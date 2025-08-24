from django.contrib import messages
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .forms import NoteForm
from .models import Note, User

# Главная страница + пагинация
def index(request):
    qs = (
        Note.objects
        .select_related("author", "status")
        .prefetch_related("categories")
        .order_by("-created_at")
    )
    paginator = Paginator(qs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "notes/index.html", {"page_obj": page_obj})

# Детальная заметка
def note_detail(request, note_id):
    qs = (
        Note.objects
        .select_related("author", "status", "author__userprofile")
        .prefetch_related("categories")
    )
    note = get_object_or_404(qs, pk=note_id)
    profile = getattr(note.author, "userprofile", None)
    return render(request, "notes/note_detail.html", {"note": note, "profile": profile})

# Создание заметки (redirect -> главная)
@login_required
@transaction.atomic
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user  # автор = текущий пользователь
            note.save()
            form.save_m2m()
            messages.success(request, f"Заметка #{note.id} создана.")
            return redirect("index")
        messages.error(request, "Пожалуйста, исправьте ошибки формы.")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form, "mode": "create"})

# Редактирование заметки (redirect -> detail)
@login_required
@transaction.atomic
def note_edit(request, note_id: int):
    note = get_object_or_404(
        Note.objects.select_related("author", "status").prefetch_related("categories"),
        pk=note_id
    )
    if not (request.user == note.author or request.user.is_staff):
        raise PermissionDenied("Доступ запрещен.")

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            messages.success(request, f"Заметка #{note.id} обновлена.")
            return redirect("note_detail", note_id=note.id)
        messages.error(request, "Пожалуйста, исправьте ошибки формы.")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form, "mode": "edit", "note": note})

# Удаление заметки
@login_required
def note_delete(request, note_id: int):
    note = get_object_or_404(Note, pk=note_id)
    if not (request.user == note.author or request.user.is_staff):
        raise PermissionDenied("Доступ запрещен.")
    if request.method == "POST":
        note.delete()
        messages.success(request, "Заметка удалена.")
        return redirect("index")
    return render(request, "notes/note_confirm_delete.html", {"note": note})

# Страница пользователя + его заметки
def user_detail(request, user_id: int):
    user = get_object_or_404(User.objects.select_related("userprofile"), pk=user_id)
    profile = getattr(user, "userprofile", None)
    user_notes = (
        Note.objects
        .filter(author=user)
        .select_related("status")
        .order_by("-created_at")
    )
    return render(request, "notes/user_detail.html", {"user": user, "profile": profile, "notes": user_notes})

# Список пользователей
def users_list(request):
    users = User.objects.all().order_by("username")
    return render(request, "notes/users_list.html", {"users": users})