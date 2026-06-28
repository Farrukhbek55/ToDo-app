import flet as ft
from datetime import datetime, date
import json
import os

BG_COLOR       = "#0F0F1A"
CARD_COLOR     = "#1A1A2E"
ACCENT         = "#7C3AED"
ACCENT_LIGHT   = "#A78BFA"
DONE_COLOR     = "#10B981"
DELETE_COLOR   = "#EF4444"
TEXT_PRIMARY   = "#F8FAFC"
TEXT_SECONDARY = "#94A3B8"
INPUT_BG       = "#16213E"
DIVIDER_COLOR  = "#2D2D44"
YELLOW         = "#F59E0B"
ORANGE         = "#F97316"

CK_TASKS = "doit_tasks"
CK_STATS = "doit_stats"

CATEGORIES = {
    "Umumiy":  "📋",
    "Ish":     "💼",
    "Shaxsiy": "👤",
    "Xarid":   "🛒",
    "Sogliq":  "❤️",
}

PRIORITIES = {
    "Oddiy":   {"color": "#64748B", "icon": "○"},
    "Ortacha": {"color": "#F59E0B", "icon": "◑"},
    "Yuqori":  {"color": "#EF4444", "icon": "●"},
}

# XP ball tizimi
XP_PER_TASK     = 10
XP_PER_PRIORITY = {"Oddiy": 10, "Ortacha": 20, "Yuqori": 35}

LEVEL_THRESHOLDS = [0, 100, 300, 600, 1000, 2000]

ACHIEVEMENTS = [
    {"id": "first",    "icon": "🎯", "req": 1},
    {"id": "ten",      "icon": "🔟", "req": 10},
    {"id": "fifty",    "icon": "💪", "req": 50},
    {"id": "streak3",  "icon": "🔥", "req": 3},
    {"id": "streak7",  "icon": "⚡", "req": 7},
    {"id": "streak30", "icon": "👑", "req": 30},
]

# ═══════════════════════════════════════════════════════════
# TARJIMA TIZIMI (i18n)
# ═══════════════════════════════════════════════════════════
LANGUAGES = {"uz": "O'zbekcha", "ru": "Русский", "en": "English"}

TR = {
    "uz": {
        "app_title": "DoIt",
        "tasks_count": "{n} ta vazifa",
        "done_count": "✓ {n} bajarildi",
        "filter_all": "Hammasi",
        "filter_active": "Aktiv",
        "filter_done": "Bajarilgan",
        "add_task_btn": "Yangi vazifa qo'shish",
        "search_hint": "Vazifa qidiring...",
        "new_task_title": "Yangi vazifa",
        "task_name_hint": "Vazifa nomi...",
        "category_label": "Kategoriya",
        "priority_label": "Muhimlik",
        "due_label": "Muddat (ixtiyoriy)",
        "time_label": "Vaqt tanlash",
        "due_not_set": "Sana tanlanmagan",
        "cancel_btn": "Bekor",
        "add_btn": "✓ Qo'shish",
        "name_required": "Vazifa nomini kiriting!",
        "achievements_title": "Yutuqlar",
        "achievements_count": "Yutuqlar ({done}/{total})",
        "total_xp": "Jami XP",
        "streak_label": "Streak",
        "completed_label": "Bajarildi",
        "goal_title": "🎯 Kunlik maqsad",
        "goal_label": "Maqsad: {n} ta",
        "goal_done": "✅ {done}/{goal} ta bajarildi",
        "goal_reached": "🎉 Maqsadga yetdingiz!",
        "goal_remaining": "{n} ta qoldi",
        "overdue": "⚠ {n}k o'tdi",
        "due_today": "⏰ Bugun",
        "due_tomorrow": "📅 Ertaga",
        "theme_tooltip": "Temani o'zgartirish",
        "search_tooltip": "Qidirish",
        "lang_tooltip": "Tilni o'zgartirish",
        "achievements_tooltip": "Yutuqlar",
        "achievement_unlocked": "🏆 Yutuq ochildi!",
        "xp_gained": "🎉 +{n} XP oldingiz!",
        "categories": {
            "Umumiy": "Umumiy", "Ish": "Ish", "Shaxsiy": "Shaxsiy",
            "Xarid": "Xarid", "Sogliq": "Sog'liq",
        },
        "priorities": {
            "Oddiy": "Oddiy", "Ortacha": "O'rtacha", "Yuqori": "Yuqori",
        },
        "levels": [
            "🌱 Yangi boshlovchi", "⚡ Faol foydalanuvchi", "🔥 Ishbilarmon",
            "💎 Ustoz", "🏆 Chempion", "🌟 Afsonaviy",
        ],
        "ach_names": {
            "first": "Birinchi qadam", "ten": "O'nta bajardim", "fifty": "Qo'l keldi",
            "streak3": "3 kunlik olov", "streak7": "Haftalik chempion", "streak30": "Oylik shoh",
        },
        "ach_descs": {
            "first": "Birinchi vazifani bajaring", "ten": "10 ta vazifani bajaring",
            "fifty": "50 ta vazifani bajaring", "streak3": "3 kun ketma-ket foydalaning",
            "streak7": "7 kun ketma-ket foydalaning", "streak30": "30 kun ketma-ket foydalaning",
        },
    },
    "ru": {
        "app_title": "DoIt",
        "tasks_count": "{n} задач",
        "done_count": "✓ {n} выполнено",
        "filter_all": "Все",
        "filter_active": "Активные",
        "filter_done": "Выполненные",
        "add_task_btn": "Добавить задачу",
        "search_hint": "Поиск задачи...",
        "new_task_title": "Новая задача",
        "task_name_hint": "Название задачи...",
        "category_label": "Категория",
        "priority_label": "Приоритет",
        "due_label": "Срок (необязательно)",
        "time_label": "Выбрать время",
        "due_not_set": "Дата не выбрана",
        "cancel_btn": "Отмена",
        "add_btn": "✓ Добавить",
        "name_required": "Введите название задачи!",
        "achievements_title": "Достижения",
        "achievements_count": "Достижения ({done}/{total})",
        "total_xp": "Всего XP",
        "streak_label": "Серия",
        "completed_label": "Выполнено",
        "goal_title": "🎯 Дневная цель",
        "goal_label": "Цель: {n}",
        "goal_done": "✅ {done}/{goal} выполнено",
        "goal_reached": "🎉 Цель достигнута!",
        "goal_remaining": "Осталось {n}",
        "overdue": "⚠ просрочено на {n}д",
        "due_today": "⏰ Сегодня",
        "due_tomorrow": "📅 Завтра",
        "theme_tooltip": "Сменить тему",
        "search_tooltip": "Поиск",
        "lang_tooltip": "Сменить язык",
        "achievements_tooltip": "Достижения",
        "achievement_unlocked": "🏆 Достижение открыто!",
        "xp_gained": "🎉 +{n} XP получено!",
        "categories": {
            "Umumiy": "Общее", "Ish": "Работа", "Shaxsiy": "Личное",
            "Xarid": "Покупки", "Sogliq": "Здоровье",
        },
        "priorities": {
            "Oddiy": "Обычный", "Ortacha": "Средний", "Yuqori": "Высокий",
        },
        "levels": [
            "🌱 Новичок", "⚡ Активный пользователь", "🔥 Деловой",
            "💎 Мастер", "🏆 Чемпион", "🌟 Легенда",
        ],
        "ach_names": {
            "first": "Первый шаг", "ten": "Десять выполнено", "fifty": "Набил руку",
            "streak3": "Серия 3 дня", "streak7": "Недельный чемпион", "streak30": "Месячный король",
        },
        "ach_descs": {
            "first": "Выполните первую задачу", "ten": "Выполните 10 задач",
            "fifty": "Выполните 50 задач", "streak3": "Используйте 3 дня подряд",
            "streak7": "Используйте 7 дней подряд", "streak30": "Используйте 30 дней подряд",
        },
    },
    "en": {
        "app_title": "DoIt",
        "tasks_count": "{n} tasks",
        "done_count": "✓ {n} completed",
        "filter_all": "All",
        "filter_active": "Active",
        "filter_done": "Completed",
        "add_task_btn": "Add new task",
        "search_hint": "Search tasks...",
        "new_task_title": "New task",
        "task_name_hint": "Task name...",
        "category_label": "Category",
        "priority_label": "Priority",
        "due_label": "Due date (optional)",
        "time_label": "Pick time",
        "due_not_set": "No date selected",
        "cancel_btn": "Cancel",
        "add_btn": "✓ Add",
        "name_required": "Please enter a task name!",
        "achievements_title": "Achievements",
        "achievements_count": "Achievements ({done}/{total})",
        "total_xp": "Total XP",
        "streak_label": "Streak",
        "completed_label": "Completed",
        "goal_title": "🎯 Daily Goal",
        "goal_label": "Goal: {n}",
        "goal_done": "✅ {done}/{goal} completed",
        "goal_reached": "🎉 Goal reached!",
        "goal_remaining": "{n} left",
        "overdue": "⚠ {n}d overdue",
        "due_today": "⏰ Today",
        "due_tomorrow": "📅 Tomorrow",
        "theme_tooltip": "Switch theme",
        "search_tooltip": "Search",
        "lang_tooltip": "Switch language",
        "achievements_tooltip": "Achievements",
        "achievement_unlocked": "🏆 Achievement unlocked!",
        "xp_gained": "🎉 +{n} XP gained!",
        "categories": {
            "Umumiy": "General", "Ish": "Work", "Shaxsiy": "Personal",
            "Xarid": "Shopping", "Sogliq": "Health",
        },
        "priorities": {
            "Oddiy": "Low", "Ortacha": "Medium", "Yuqori": "High",
        },
        "levels": [
            "🌱 Beginner", "⚡ Active User", "🔥 Go-Getter",
            "💎 Master", "🏆 Champion", "🌟 Legend",
        ],
        "ach_names": {
            "first": "First Step", "ten": "Ten Done", "fifty": "Getting Good",
            "streak3": "3-Day Streak", "streak7": "Weekly Champion", "streak30": "Monthly King",
        },
        "ach_descs": {
            "first": "Complete your first task", "ten": "Complete 10 tasks",
            "fifty": "Complete 50 tasks", "streak3": "Use the app 3 days in a row",
            "streak7": "Use the app 7 days in a row", "streak30": "Use the app 30 days in a row",
        },
    },
}

def t(lang, key, **kwargs):
    """Tarjima matnini olish. kwargs orqali {n}, {done} kabi joylar to'ldiriladi."""
    text = TR.get(lang, TR["uz"]).get(key, key)
    if kwargs:
        try:
            text = text.format(**kwargs)
        except Exception:
            pass
    return text

def t_cat(lang, cat_key):
    """Kategoriya nomini tarjima qilish (kalit o'zgarmaydi, faqat ko'rinish)"""
    return TR.get(lang, TR["uz"])["categories"].get(cat_key, cat_key)

def t_pri(lang, pri_key):
    """Muhimlik nomini tarjima qilish"""
    return TR.get(lang, TR["uz"])["priorities"].get(pri_key, pri_key)

def t_level(lang, index):
    """Daraja nomini tarjima qilish"""
    levels = TR.get(lang, TR["uz"])["levels"]
    return levels[min(index, len(levels) - 1)]

def t_ach_name(lang, ach_id):
    return TR.get(lang, TR["uz"])["ach_names"].get(ach_id, ach_id)

def t_ach_desc(lang, ach_id):
    return TR.get(lang, TR["uz"])["ach_descs"].get(ach_id, ach_id)


def make_border(color):
    s = ft.BorderSide(1, color)
    return ft.Border(top=s, bottom=s, left=s, right=s)

def load_tasks(page):
    try:
        data = page.client_storage.get(CK_TASKS)
        if data:
            return data
    except Exception:
        pass
    return []

def save_tasks(page, data):
    try:
        page.client_storage.set(CK_TASKS, data)
    except Exception:
        pass

def load_stats(page):
    default = {
        "xp": 0,
        "total_done": 0,
        "streak": 0,
        "last_date": "",
        "achievements": [],
    }
    try:
        raw = page.client_storage.get(CK_STATS)
        if raw:
            data = raw
            for k, v in default.items():
                if k not in data:
                    data[k] = v
            return data
    except Exception:
        pass
    return default

def save_stats(page, data):
    try:
        page.client_storage.set(CK_STATS, data)
    except Exception:
        pass

def get_level_index(xp):
    """XP ga mos daraja indeksini qaytaradi (0-5)"""
    idx = 0
    for i, min_xp in enumerate(LEVEL_THRESHOLDS):
        if xp >= min_xp:
            idx = i
    return idx

def get_level_progress(xp):
    thresholds = LEVEL_THRESHOLDS
    for i in range(len(thresholds) - 1):
        if xp < thresholds[i + 1]:
            start = thresholds[i]
            end   = thresholds[i + 1]
            return (xp - start) / (end - start)
    return 1.0

def update_streak(stats):
    today = date.today().isoformat()
    last  = stats.get("last_date", "")
    if last == today:
        return stats
    if last:
        try:
            last_d = date.fromisoformat(last)
            diff   = (date.today() - last_d).days
            if diff == 1:
                stats["streak"] = stats.get("streak", 0) + 1
            elif diff > 1:
                stats["streak"] = 1
        except Exception:
            stats["streak"] = 1
    else:
        stats["streak"] = 1
    stats["last_date"] = today
    return stats


class Task(ft.Container):
    def __init__(self, task_name, task_delete, on_change,
                 created_at=None, is_done=False,
                 category="Umumiy", priority="Oddiy", due_date=None,
                 lang="uz",
        ):
        super().__init__()
        self.task_name   = task_name
        self.task_delete = task_delete
        self.on_change   = on_change
        self.is_done     = is_done
        self.created_at  = created_at or datetime.now().strftime("%H:%M")
        self.category    = category
        self.priority    = priority
        self.due_date    = due_date
        self.lang        = lang

        cat_icon = CATEGORIES.get(self.category, "📋")
        pri      = PRIORITIES.get(self.priority, PRIORITIES["Oddiy"])

        self.cb = ft.Checkbox(
            value=self.is_done,
            fill_color={
                ft.ControlState.SELECTED: DONE_COLOR,
                ft.ControlState.DEFAULT:  "transparent",
            },
            check_color="#FFFFFF",
            on_change=self.toggle_done,
        )

        self.task_text = ft.Text(
            self.task_name,
            color=TEXT_SECONDARY if self.is_done else TEXT_PRIMARY,
            size=14,
            expand=True,
            style=ft.TextStyle(
                decoration=ft.TextDecoration.LINE_THROUGH if self.is_done
                           else ft.TextDecoration.NONE
            ),
        )

        tag_controls = [
            ft.Container(
                content=ft.Text(f"{cat_icon} {t_cat(self.lang, self.category)}", size=10, color=ACCENT_LIGHT),
                bgcolor=ACCENT + "20", border_radius=6, padding=4,
            ),
            ft.Container(
                content=ft.Text(f"{pri['icon']} {t_pri(self.lang, self.priority)}", size=10, color=pri["color"]),
                bgcolor=pri["color"] + "20", border_radius=6, padding=4,
            ),
        ]

        if self.due_date:
            try:
                # due_date "YYYY-MM-DD" yoki "YYYY-MM-DD HH:MM" bo'lishi mumkin
                date_part = self.due_date.split(" ")[0]
                time_part = self.due_date.split(" ")[1] if " " in self.due_date else None

                due  = datetime.strptime(date_part, "%Y-%m-%d").date()
                diff = (due - date.today()).days

                time_suffix = f" {time_part}" if time_part else ""

                if diff < 0:
                    dc, dl = DELETE_COLOR, t(self.lang, "overdue", n=abs(diff))
                elif diff == 0:
                    dc, dl = YELLOW, t(self.lang, "due_today") + time_suffix
                elif diff == 1:
                    dc, dl = YELLOW, t(self.lang, "due_tomorrow") + time_suffix
                else:
                    dc, dl = TEXT_SECONDARY, f"📅 {self.due_date}"
                tag_controls.append(
                    ft.Container(
                        content=ft.Text(dl, size=10, color=dc),
                        bgcolor=dc + "20", border_radius=6, padding=4,
                    )
                )
            except Exception:
                pass

        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.cb,
                        self.task_text,
                        ft.IconButton(
                            icon=ft.Icons.DELETE_ROUNDED,
                            icon_color=DELETE_COLOR,
                            icon_size=18,
                            on_click=self.delete_clicked,
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(controls=tag_controls, spacing=6),
            ],
            spacing=6,
        )

        self.bgcolor       = "#0D2818" if self.is_done else CARD_COLOR
        self.border_radius = 14
        self.padding       = 12
        self.border        = make_border(DONE_COLOR if self.is_done else DIVIDER_COLOR)

    def toggle_done(self, e):
        self.is_done = self.cb.value
        if self.is_done:
            self.task_text.color = TEXT_SECONDARY
            self.task_text.style = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)
            self.border  = make_border(DONE_COLOR)
            self.bgcolor = "#0D2818"
        else:
            self.task_text.color = TEXT_PRIMARY
            self.task_text.style = ft.TextStyle(decoration=ft.TextDecoration.NONE)
            self.border  = make_border(DIVIDER_COLOR)
            self.bgcolor = CARD_COLOR
        self.update()
        self.on_change(self.priority if self.is_done else None)

    def delete_clicked(self, e):
        self.task_delete(self)

    def to_dict(self):
        return {
            "name":       self.task_name,
            "is_done":    self.is_done,
            "created_at": self.created_at,
            "category":   self.category,
            "priority":   self.priority,
            "due_date":   self.due_date,
        }


def main(page: ft.Page):
    page.title         = "DoIt"
    page.bgcolor       = BG_COLOR
    page.padding       = 0
    page.scroll        = ft.ScrollMode.HIDDEN
    page.theme_mode    = ft.ThemeMode.DARK
    page.window.width  = 420
    page.window.height = 760

    # ── Til tizimi ───────────────────────────────────────────
    def load_lang():
        try:
            data = page.client_storage.get("doit_lang")
            if data in TR:
                return data
        except Exception:
            pass
        return "uz"

    def save_lang(lang_code):
        try:
            page.client_storage.set("doit_lang", lang_code)
        except Exception:
            pass

    current_lang = [load_lang()]

    def L(key, **kwargs):
        """Joriy tilda matn olish uchun qisqa nom"""
        return t(current_lang[0], key, **kwargs)

    stats      = load_stats(page)
    stats      = update_streak(stats)
    tasks_list = ft.Column(spacing=10)

    # ── Statistika matnlari ─────────────────────────────────
    xp_text      = ft.Text(f"⭐ {stats['xp']} XP", color=YELLOW, size=13, weight=ft.FontWeight.BOLD)
    level_text   = ft.Text(t_level(current_lang[0], get_level_index(stats["xp"])), color=ACCENT_LIGHT, size=12)
    streak_text  = ft.Text(f"🔥 {stats['streak']}", color=ORANGE, size=13, weight=ft.FontWeight.BOLD)
    counter_text = ft.Text(L("tasks_count", n=0), color=TEXT_SECONDARY, size=13)
    done_text    = ft.Text("", color=DONE_COLOR, size=13)

    xp_bar = ft.Container(
        content=ft.Container(
            bgcolor=ACCENT,
            border_radius=4,
            width=0,
        ),
        bgcolor=DIVIDER_COLOR,
        border_radius=4,
        height=6,
        expand=True,
    )

    def refresh_stats_ui():
        xp_text.value    = f"⭐ {stats['xp']} XP"
        level_text.value = t_level(current_lang[0], get_level_index(stats["xp"]))
        streak_text.value = f"🔥 {stats['streak']}"
        progress = get_level_progress(stats["xp"])
        xp_bar.content.width = max(4, int(340 * progress))
        xp_text.update()
        level_text.update()
        streak_text.update()
        xp_bar.content.update()

    def check_achievements():
        new_unlocked = []
        for ach in ACHIEVEMENTS:
            if ach["id"] in stats["achievements"]:
                continue
            unlocked = False
            if ach["id"] == "first"    and stats["total_done"] >= 1:  unlocked = True
            if ach["id"] == "ten"      and stats["total_done"] >= 10: unlocked = True
            if ach["id"] == "fifty"    and stats["total_done"] >= 50: unlocked = True
            if ach["id"] == "streak3"  and stats["streak"] >= 3:      unlocked = True
            if ach["id"] == "streak7"  and stats["streak"] >= 7:      unlocked = True
            if ach["id"] == "streak30" and stats["streak"] >= 30:     unlocked = True
            if unlocked:
                stats["achievements"].append(ach["id"])
                new_unlocked.append(ach)
        return new_unlocked

    def show_achievement(ach):
        notif = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(ach["icon"], size=24),
                    ft.Column(
                        controls=[
                            ft.Text(L("achievement_unlocked"), color=YELLOW, size=11, weight=ft.FontWeight.BOLD),
                            ft.Text(t_ach_name(current_lang[0], ach["id"]), color=TEXT_PRIMARY, size=13, weight=ft.FontWeight.BOLD),
                            ft.Text(t_ach_desc(current_lang[0], ach["id"]), color=TEXT_SECONDARY, size=11),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#1C1033",
            border_radius=14,
            padding=14,
            border=make_border(ACCENT),
            shadow=ft.BoxShadow(blur_radius=20, color=ACCENT + "60", offset=ft.Offset(0, 4)),
        )
        page.overlay.append(
            ft.Container(
                content=notif,
                top=60,
                right=16,
                left=16,
            )
        )
        page.update()

        import threading
        def remove():
            import time
            time.sleep(3)
            if page.overlay:
                page.overlay.pop()
                page.update()
        threading.Thread(target=remove, daemon=True).start()

    def update_stats_data(priority=None):
        if priority:
            xp_gain = XP_PER_PRIORITY.get(priority, XP_PER_TASK)
            stats["xp"]         += xp_gain
            stats["total_done"] += 1
        new_ach = check_achievements()
        save_stats(page, stats)
        refresh_stats_ui()
        for ach in new_ach:
            show_achievement(ach)

    # ── Tema tizimi ─────────────────────────────────────────
    def load_theme():
        try:
            data = page.client_storage.get("doit_theme")
            if data is not None:
                return data.get("dark", True)
        except Exception:
            pass
        return True

    def save_theme(dark):
        try:
            page.client_storage.set("doit_theme", {"dark": dark})
        except Exception:
            pass

    is_dark = [load_theme()]

    # Yorug' tema ranglari
    L_BG      = "#F8FAFC"
    L_CARD    = "#FFFFFF"
    L_INPUT   = "#F1F5F9"
    L_DIVIDER = "#E2E8F0"
    L_TEXT    = "#1E293B"
    L_TEXT2   = "#64748B"

    app_title_text = ft.Text("DoIt", size=26, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY)
    ach_title_text = ft.Text(L("achievements_title"), size=22, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY)
    date_text      = ft.Text(datetime.now().strftime("%d %B, %Y"), size=12, color=TEXT_SECONDARY)

    theme_icon_btn = ft.IconButton(
        icon=ft.Icons.DARK_MODE_ROUNDED if is_dark[0] else ft.Icons.LIGHT_MODE_ROUNDED,
        icon_color=ACCENT_LIGHT,
        icon_size=22,
        tooltip=L("theme_tooltip"),
        on_click=lambda e: safe_toggle_theme(),
    )

    def change_language(lang_code):
        current_lang[0] = lang_code
        save_lang(lang_code)
        try:
            refresh_all_text()
        except Exception as ex:
            import traceback
            print("LANG SWITCH ERROR:", ex)
            traceback.print_exc()

    lang_icon_btn = ft.PopupMenuButton(
        icon=ft.Icons.LANGUAGE_ROUNDED,
        icon_color=TEXT_SECONDARY,
        icon_size=22,
        tooltip=L("lang_tooltip"),
        items=[
            ft.PopupMenuItem(content=ft.Text("O'zbekcha"), on_click=lambda e: change_language("uz")),
            ft.PopupMenuItem(content=ft.Text("Русский"), on_click=lambda e: change_language("ru")),
            ft.PopupMenuItem(content=ft.Text("English"), on_click=lambda e: change_language("en")),
        ],
    )

    def safe_toggle_theme():
        try:
            toggle_theme()
        except Exception as ex:
            import traceback
            print("THEME ERROR:", ex)
            traceback.print_exc()

    def apply_task_theme(task):
        dark = is_dark[0]
        if task.is_done:
            task.bgcolor        = "#0D2818" if dark else "#DCFCE7"
            task.task_text.color= TEXT_SECONDARY if dark else L_TEXT2
            task.border         = make_border(DONE_COLOR)
        else:
            task.bgcolor        = CARD_COLOR if dark else L_CARD
            task.task_text.color= TEXT_PRIMARY if dark else L_TEXT
            task.border         = make_border(DIVIDER_COLOR if dark else L_DIVIDER)
        task.update()

    def tv(dark, d, l):
        """dark rejimda d, yorug'da l qaytaradi"""
        return d if dark else l

    def toggle_theme():
        is_dark[0] = not is_dark[0]
        save_theme(is_dark[0])
        dark = is_dark[0]

        page.bgcolor    = tv(dark, BG_COLOR, L_BG)
        page.theme_mode = ft.ThemeMode.DARK if dark else ft.ThemeMode.LIGHT

        theme_icon_btn.icon       = ft.Icons.DARK_MODE_ROUNDED if dark else ft.Icons.LIGHT_MODE_ROUNDED
        theme_icon_btn.icon_color = tv(dark, ACCENT_LIGHT, ACCENT)

        app_title_text.color = tv(dark, TEXT_PRIMARY, L_TEXT)
        ach_title_text.color = tv(dark, TEXT_PRIMARY, L_TEXT)
        date_text.color      = tv(dark, TEXT_SECONDARY, L_TEXT2)

        counter_text.color = tv(dark, TEXT_SECONDARY, L_TEXT2)
        done_text.color    = DONE_COLOR
        xp_text.color      = YELLOW
        streak_text.color  = ORANGE
        level_text.color   = tv(dark, ACCENT_LIGHT, ACCENT)

        header.bgcolor = tv(dark, BG_COLOR, L_BG)
        main_view_container.bgcolor = tv(dark, BG_COLOR, L_BG)
        ach_page_container.bgcolor  = tv(dark, BG_COLOR, L_BG)

        goal_placeholder.bgcolor = tv(dark, CARD_COLOR, L_CARD)
        goal_num_txt.color       = tv(dark, TEXT_SECONDARY, L_TEXT2)
        goal_done_txt.color      = DONE_COLOR
        goal_pct_txt.color       = tv(dark, TEXT_SECONDARY, L_TEXT2)

        xp_bar.bgcolor = tv(dark, DIVIDER_COLOR, L_DIVIDER)

        search_field.bgcolor      = tv(dark, INPUT_BG, L_INPUT)
        search_field.border_color = tv(dark, DIVIDER_COLOR, L_DIVIDER)
        search_field.color        = tv(dark, TEXT_PRIMARY, L_TEXT)
        search_field.hint_style   = ft.TextStyle(color=tv(dark, TEXT_SECONDARY, L_TEXT2))

        form_panel.bgcolor      = tv(dark, CARD_COLOR, L_CARD)
        name_field.bgcolor      = tv(dark, INPUT_BG, L_INPUT)
        name_field.color        = tv(dark, TEXT_PRIMARY, L_TEXT)
        name_field.border_color = tv(dark, DIVIDER_COLOR, L_DIVIDER)
        due_field.bgcolor       = tv(dark, INPUT_BG, L_INPUT)
        due_field.color         = tv(dark, TEXT_PRIMARY, L_TEXT)
        due_field.border_color  = tv(dark, DIVIDER_COLOR, L_DIVIDER)
        cat_dropdown.bgcolor    = tv(dark, INPUT_BG, L_INPUT)
        cat_dropdown.color      = tv(dark, TEXT_PRIMARY, L_TEXT)
        pri_dropdown.bgcolor    = tv(dark, INPUT_BG, L_INPUT)
        pri_dropdown.color      = tv(dark, TEXT_PRIMARY, L_TEXT)

        for btn in filter_btns:
            try:
                active = bool(btn.style) and btn.style.color == ACCENT
            except Exception:
                active = False
            btn.style = ft.ButtonStyle(
                color=ACCENT if active else tv(dark, TEXT_SECONDARY, L_TEXT2)
            )

        add_bar_container.bgcolor = tv(dark, BG_COLOR, L_BG)
        add_bar_inner.bgcolor     = tv(dark, ACCENT + "15", ACCENT + "10")
        add_bar_inner.border      = make_border(ACCENT + "40")
        add_bar_label.color       = tv(dark, ACCENT_LIGHT, ACCENT)
        add_bar_icon.color        = tv(dark, ACCENT_LIGHT, ACCENT)

        for task in tasks_list.controls:
            task.is_done = task.cb.value
            if task.is_done:
                task.bgcolor         = "#0D2818" if dark else "#DCFCE7"
                task.task_text.color = TEXT_SECONDARY if dark else L_TEXT2
                task.border          = make_border(DONE_COLOR)
            else:
                task.bgcolor         = CARD_COLOR if dark else L_CARD
                task.task_text.color = TEXT_PRIMARY if dark else L_TEXT
                task.border          = make_border(DIVIDER_COLOR if dark else L_DIVIDER)

        page.update()

    def update_counts():
        total = len(tasks_list.controls)
        done  = sum(1 for t in tasks_list.controls if t.is_done)
        counter_text.value = L("tasks_count", n=total)
        done_text.value    = L("done_count", n=done) if done > 0 else ""
        counter_text.update()
        done_text.update()

    def persist(priority=None):
        save_tasks(page, [t.to_dict() for t in tasks_list.controls])
        update_stats_data(priority)
        update_counts()
        try:
            refresh_goal_ui()
        except Exception:
            pass

    def delete_task(task):
        tasks_list.controls.remove(task)
        save_tasks(page, [t.to_dict() for t in tasks_list.controls])
        update_counts()
        page.update()

    # ── Forma maydonlari ────────────────────────────────────
    name_field = ft.TextField(
        hint_text=L("task_name_hint"),
        hint_style=ft.TextStyle(color=TEXT_SECONDARY),
        color=TEXT_PRIMARY, bgcolor=INPUT_BG,
        border_color=DIVIDER_COLOR, focused_border_color=ACCENT_LIGHT,
        border_radius=10, text_size=14, content_padding=12,
    )
    due_field = ft.TextField(
        hint_text=L("due_not_set"),
        hint_style=ft.TextStyle(color=TEXT_SECONDARY),
        color=TEXT_PRIMARY, bgcolor=INPUT_BG,
        border_color=DIVIDER_COLOR, focused_border_color=ACCENT_LIGHT,
        border_radius=10, text_size=13, content_padding=10,
        read_only=True,
        expand=True,
    )

    # Tanlangan sana va vaqtni alohida saqlaymiz, due_field faqat ko'rsatish uchun
    due_state = {"date": None, "time": None}

    def rebuild_due_field():
        """due_state ga qarab due_field matnini yig'adi: YYYY-MM-DD HH:MM yoki faqat YYYY-MM-DD"""
        if due_state["date"] and due_state["time"]:
            due_field.value = f"{due_state['date']} {due_state['time']}"
        elif due_state["date"]:
            due_field.value = due_state["date"]
        else:
            due_field.value = ""
        due_field.update()

    def on_date_picked(e):
        try:
            if date_picker.value:
                d = date_picker.value
                # Flet DatePicker mahalliy kunni UTC ga aylantirib yuboradi,
                # natijada UTC kuni 1 kun orqada chiqadi (masalan 19:00 UTC).
                # Buni mahalliy taqvim kuniga qaytarish uchun bir kun qo'shamiz.
                from datetime import timedelta
                d_fixed = d + timedelta(days=1)
                due_state["date"] = f"{d_fixed.year:04d}-{d_fixed.month:02d}-{d_fixed.day:02d}"
                rebuild_due_field()
        except Exception as ex:
            print("DATE PICKER ERROR:", ex)

    def on_time_picked(e):
        try:
            if time_picker.value:
                tm = time_picker.value
                due_state["time"] = f"{tm.hour:02d}:{tm.minute:02d}"
                rebuild_due_field()
        except Exception as ex:
            print("TIME PICKER ERROR:", ex)

    date_picker = ft.DatePicker(
        first_date=date.today(),
        last_date=date(date.today().year + 2, 12, 31),
        on_change=on_date_picked,
    )
    page.overlay.append(date_picker)

    time_picker = ft.TimePicker(
        on_change=on_time_picked,
    )
    page.overlay.append(time_picker)

    def open_date_picker(e):
        date_picker.open = True
        page.update()

    def open_time_picker(e):
        time_picker.open = True
        page.update()

    def clear_due_date(e):
        due_state["date"] = None
        due_state["time"] = None
        rebuild_due_field()

    due_field_row = ft.Row(
        controls=[
            due_field,
            ft.IconButton(
                icon=ft.Icons.CALENDAR_MONTH_ROUNDED,
                icon_color=ACCENT_LIGHT,
                icon_size=20,
                tooltip=L("due_label"),
                on_click=open_date_picker,
            ),
            ft.IconButton(
                icon=ft.Icons.ACCESS_TIME_ROUNDED,
                icon_color=ACCENT_LIGHT,
                icon_size=20,
                tooltip=L("time_label"),
                on_click=open_time_picker,
            ),
            ft.IconButton(
                icon=ft.Icons.CLOSE_ROUNDED,
                icon_color=TEXT_SECONDARY,
                icon_size=18,
                tooltip=L("due_not_set"),
                on_click=clear_due_date,
            ),
        ],
        spacing=4,
    )
    cat_dropdown = ft.Dropdown(
        value="Umumiy",
        options=[ft.dropdown.Option(k, f"{v} {t_cat(current_lang[0], k)}") for k, v in CATEGORIES.items()],
        bgcolor=INPUT_BG, color=TEXT_PRIMARY,
        border_color=DIVIDER_COLOR, focused_border_color=ACCENT_LIGHT,
        border_radius=10, text_size=13, content_padding=10,
    )
    pri_dropdown = ft.Dropdown(
        value="Oddiy",
        options=[ft.dropdown.Option(k, f"{v['icon']} {t_pri(current_lang[0], k)}") for k, v in PRIORITIES.items()],
        bgcolor=INPUT_BG, color=TEXT_PRIMARY,
        border_color=DIVIDER_COLOR, focused_border_color=ACCENT_LIGHT,
        border_radius=10, text_size=13, content_padding=10,
    )

    def add_task(e):
        val = name_field.value.strip()
        if not val:
            name_field.error_text  = L("name_required")
            name_field.border_color = DELETE_COLOR
            name_field.focused_border_color = DELETE_COLOR
            name_field.update()
            name_field.focus()
            return
        name_field.error_text  = None
        name_field.border_color = DIVIDER_COLOR
        name_field.focused_border_color = ACCENT_LIGHT
        new_task = Task(
            task_name   = val,
            task_delete = delete_task,
            on_change   = persist,
            category    = cat_dropdown.value or "Umumiy",
            priority    = pri_dropdown.value or "Oddiy",
            due_date    = due_field.value.strip() or None,
            lang        = current_lang[0],
        )
        tasks_list.controls.insert(0, new_task)
        form_panel.visible = False
        form_panel.update()
        save_tasks(page, [t.to_dict() for t in tasks_list.controls])
        update_counts()
        page.update()

    def toggle_form(show):
        form_panel.visible = show
        if show:
            name_field.value = ""
            due_field.value  = ""
            due_state["date"] = None
            due_state["time"] = None
            name_field.error_text  = None
            name_field.border_color = DIVIDER_COLOR
            name_field.focused_border_color = ACCENT_LIGHT
            cat_dropdown.value = "Umumiy"
            pri_dropdown.value = "Oddiy"
        form_panel.update()
        if show:
            name_field.focus()

    form_title_text    = ft.Text(L("new_task_title"), color=TEXT_PRIMARY, size=15, weight=ft.FontWeight.BOLD)
    form_cat_label      = ft.Text(L("category_label"), color=TEXT_SECONDARY, size=11)
    form_pri_label      = ft.Text(L("priority_label"), color=TEXT_SECONDARY, size=11)
    form_due_label      = ft.Text(L("due_label"), color=TEXT_SECONDARY, size=11)

    form_cancel_text = ft.Text(L("cancel_btn"))
    form_cancel_btn  = ft.TextButton(
        content=form_cancel_text,
        on_click=lambda e: toggle_form(False),
        style=ft.ButtonStyle(color=TEXT_SECONDARY),
    )

    form_add_text = ft.Text(L("add_btn"))
    form_add_btn  = ft.ElevatedButton(
        content=form_add_text,
        on_click=add_task,
        bgcolor=ACCENT, color=TEXT_PRIMARY,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
    )

    form_panel = ft.Container(
        visible=False,
        bgcolor=CARD_COLOR, border_radius=16, padding=16,
        border=make_border(ACCENT + "50"),
        content=ft.Column(
            controls=[
                form_title_text,
                name_field,
                ft.Row(
                    controls=[
                        ft.Column(controls=[form_cat_label, cat_dropdown], expand=True, spacing=4),
                        ft.Column(controls=[form_pri_label, pri_dropdown], expand=True, spacing=4),
                    ],
                    spacing=10,
                ),
                form_due_label,
                due_field_row,
                ft.Row(
                    controls=[
                        form_cancel_btn,
                        ft.Container(expand=True),
                        form_add_btn,
                    ],
                ),
            ],
            spacing=10,
        ),
    )


    # ── Yutuqlar ekrani ─────────────────────────────────────
    def show_achievements_screen(e):
        dark = is_dark[0]
        d_card = tv(dark, CARD_COLOR, L_CARD)
        d_bg   = tv(dark, BG_COLOR, L_BG)
        d_text = tv(dark, TEXT_PRIMARY, L_TEXT)
        d_sec  = tv(dark, TEXT_SECONDARY, L_TEXT2)
        d_div  = tv(dark, DIVIDER_COLOR, L_DIVIDER)

        ach_controls = []
        for ach in ACHIEVEMENTS:
            unlocked = ach["id"] in stats["achievements"]
            ach_controls.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(ach["icon"] if unlocked else "🔒", size=28),
                            ft.Column(
                                controls=[
                                    ft.Text(t_ach_name(current_lang[0], ach["id"]), color=d_text if unlocked else d_sec,
                                            size=14, weight=ft.FontWeight.BOLD),
                                    ft.Text(t_ach_desc(current_lang[0], ach["id"]), color=d_sec, size=12),
                                ],
                                spacing=2, expand=True,
                            ),
                            ft.Text("✓", color=DONE_COLOR, size=18) if unlocked else ft.Text(""),
                        ],
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=d_card if unlocked else d_bg,
                    border_radius=12, padding=14,
                    border=make_border(DONE_COLOR + "60" if unlocked else d_div),
                    opacity=1.0 if unlocked else 0.5,
                )
            )

        ach_page.controls = [
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Container(height=40),
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.ARROW_BACK_ROUNDED,
                                    icon_color=d_text,
                                    on_click=lambda e: switch_view("main"),
                                ),
                                ach_title_text,
                            ],
                            spacing=8,
                        ),
                        ft.Container(height=4),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Text(L("total_xp"), color=d_sec, size=11),
                                                    ft.Text(f"⭐ {stats['xp']}", color=YELLOW, size=20, weight=ft.FontWeight.BOLD),
                                                ],
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                expand=True,
                                            ),
                                            ft.Column(
                                                controls=[
                                                    ft.Text(L("streak_label"), color=d_sec, size=11),
                                                    ft.Text(f"🔥 {stats['streak']}", color=ORANGE, size=20, weight=ft.FontWeight.BOLD),
                                                ],
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                expand=True,
                                            ),
                                            ft.Column(
                                                controls=[
                                                    ft.Text(L("completed_label"), color=d_sec, size=11),
                                                    ft.Text(f"✅ {stats['total_done']}", color=DONE_COLOR, size=20, weight=ft.FontWeight.BOLD),
                                                ],
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                expand=True,
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            bgcolor=d_card, border_radius=14, padding=16,
                        ),
                        ft.Container(height=8),
                        ft.Text(L("achievements_count", done=len(stats['achievements']), total=len(ACHIEVEMENTS)),
                                color=d_sec, size=13),
                        ft.Container(height=4),
                        ft.Column(controls=ach_controls, spacing=8, scroll=ft.ScrollMode.AUTO),
                    ],
                    spacing=8,
                    scroll=ft.ScrollMode.AUTO,
                ),
                padding=20,
                expand=True,
                bgcolor=d_bg,
            )
        ]
        ach_page_container.bgcolor = d_bg
        switch_view("achievements")

    ach_page = ft.Column(controls=[], expand=True)
    ach_page_container = ft.Container(content=ach_page, bgcolor=BG_COLOR, expand=True, visible=False)

    def switch_view(view):
        main_view_container.visible = (view == "main")
        ach_page_container.visible  = (view == "achievements")
        main_view_container.update()
        ach_page_container.update()

    # ── Filtr ───────────────────────────────────────────────
    filter_all_text    = ft.Text(L("filter_all"))
    filter_active_text = ft.Text(L("filter_active"))
    filter_done_text    = ft.Text(L("filter_done"))

    filter_btns = [
        ft.TextButton(content=filter_all_text,    data="Hammasi",    on_click=lambda e: apply_filter(e.control.data), style=ft.ButtonStyle(color=ACCENT)),
        ft.TextButton(content=filter_active_text, data="Aktiv",      on_click=lambda e: apply_filter(e.control.data), style=ft.ButtonStyle(color=TEXT_SECONDARY)),
        ft.TextButton(content=filter_done_text,   data="Bajarilgan", on_click=lambda e: apply_filter(e.control.data), style=ft.ButtonStyle(color=TEXT_SECONDARY)),
    ]

    def apply_filter(f):
        for btn in filter_btns:
            btn.style = ft.ButtonStyle(color=ACCENT if btn.data == f else TEXT_SECONDARY)
            btn.update()
        for task in tasks_list.controls:
            task.visible = True if f == "Hammasi" else (not task.is_done if f == "Aktiv" else task.is_done)
            task.update()

    # ── Header ──────────────────────────────────────────────
    goal_placeholder = ft.Container(expand=False)

    header = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(height=36),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text("✦", size=20, color=ACCENT_LIGHT),
                            bgcolor=ACCENT + "25", border_radius=10, padding=8,
                        ),
                        ft.Column(
                            controls=[
                                app_title_text,
                                date_text,
                            ],
                            spacing=2, expand=True,
                        ),
                        theme_icon_btn,
                        lang_icon_btn,
                        ft.IconButton(
                            icon=ft.Icons.SEARCH_ROUNDED,
                            icon_color=TEXT_SECONDARY,
                            icon_size=22,
                            tooltip=L("search_tooltip"),
                            on_click=lambda e: toggle_search(e),
                        ),
                        ft.IconButton(
                            icon=ft.Icons.EMOJI_EVENTS_ROUNDED,
                            icon_color=YELLOW,
                            icon_size=24,
                            tooltip=L("achievements_tooltip"),
                            on_click=lambda e: show_achievements_screen(e),
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12,
                ),
                ft.Container(height=8),
                # XP va Streak qatori
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    xp_text,
                                    ft.Container(expand=True),
                                    streak_text,
                                ],
                            ),
                            ft.Row(controls=[level_text], spacing=4),
                            ft.Container(height=4),
                            xp_bar,
                        ],
                        spacing=4,
                    ),
                    bgcolor=CARD_COLOR, border_radius=12, padding=12,
                ),
                ft.Container(height=6),
                ft.Row(controls=[counter_text, ft.Container(expand=True), done_text]),
                ft.Container(height=4),
                ft.Row(controls=filter_btns, spacing=0),
                ft.Container(height=4),
                goal_placeholder,
            ],
            spacing=2,
        ),
        padding=20,
    )

    divider_bar = ft.Container(
        gradient=ft.LinearGradient(
            colors=[ACCENT, ACCENT_LIGHT, "#00000000"],
            begin=ft.Alignment(-1, 0), end=ft.Alignment(1, 0),
        ),
        height=2, border_radius=2,
    )

    add_bar_icon  = ft.Icon(ft.Icons.ADD_CIRCLE_OUTLINE_ROUNDED, color=ACCENT_LIGHT, size=18)
    add_bar_label = ft.Text(L("add_task_btn"), color=ACCENT_LIGHT, size=14)
    add_bar_inner = ft.Container(
        content=ft.Row(controls=[add_bar_icon, add_bar_label], spacing=8),
        bgcolor=ACCENT + "15", border_radius=12, padding=14,
        on_click=lambda e: toggle_form(True),
        border=make_border(ACCENT + "40"),
    )
    add_bar_container = ft.Container(content=add_bar_inner, padding=20)
    add_bar = add_bar_container

    tasks_section = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(content=form_panel, padding=20),
                ft.Container(content=tasks_list, padding=20),
            ],
            scroll=ft.ScrollMode.AUTO,
        ),
        expand=True,
    )

    # ── Kunlik maqsad ──────────────────────────────────────
    def load_goal():
        try:
            data = page.client_storage.get("doit_goal")
            if data is not None and data.get("date") == date.today().isoformat():
                return data
        except Exception:
            pass
        return {"date": date.today().isoformat(), "goal": 5}

    def save_goal(goal_num):
        try:
            page.client_storage.set(
                "doit_goal",
                {"date": date.today().isoformat(), "goal": goal_num},
            )
        except Exception:
            pass

    goal_data = load_goal()

    def get_today_done():
        today = date.today().isoformat()
        return sum(1 for t in tasks_list.controls if t.is_done)

    # Kunlik maqsad widgetlari
    goal_num      = [goal_data.get("goal", 5)]
    goal_done_txt = ft.Text("", color=DONE_COLOR, size=13, weight=ft.FontWeight.BOLD)
    goal_pct_txt  = ft.Text("", color=TEXT_SECONDARY, size=11)
    goal_bar_fill = ft.Container(bgcolor=ACCENT, border_radius=6, width=0, height=10)
    goal_bar      = ft.Container(
        content=goal_bar_fill,
        bgcolor=DIVIDER_COLOR,
        border_radius=6,
        height=10,
        expand=True,
    )
    goal_num_txt  = ft.Text(L("goal_label", n=goal_num[0]), color=TEXT_SECONDARY, size=12)

    def refresh_goal_ui():
        done  = get_today_done()
        goal  = goal_num[0]
        pct   = min(done / goal, 1.0) if goal > 0 else 0
        width = int(320 * pct)

        goal_bar_fill.width  = max(0, width)
        goal_bar_fill.bgcolor = DONE_COLOR if pct >= 1.0 else ACCENT
        goal_done_txt.value  = L("goal_done", done=done, goal=goal)
        goal_pct_txt.value   = f"{int(pct*100)}% — " + (
            L("goal_reached") if pct >= 1.0 else
            L("goal_remaining", n=goal - done)
        )
        goal_num_txt.value   = L("goal_label", n=goal)
        try:
            goal_bar_fill.update()
            goal_done_txt.update()
            goal_pct_txt.update()
            goal_num_txt.update()
        except Exception:
            pass

    def change_goal(delta):
        goal_num[0] = max(1, min(20, goal_num[0] + delta))
        save_goal(goal_num[0])
        refresh_goal_ui()

    goal_title_text = ft.Text(L("goal_title"), color=TEXT_PRIMARY,
                               size=14, weight=ft.FontWeight.BOLD)

    goal_card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        goal_title_text,
                        ft.Container(expand=True),
                        ft.IconButton(
                            icon=ft.Icons.REMOVE_ROUNDED,
                            icon_color=TEXT_SECONDARY,
                            icon_size=18,
                            on_click=lambda e: change_goal(-1),
                        ),
                        goal_num_txt,
                        ft.IconButton(
                            icon=ft.Icons.ADD_ROUNDED,
                            icon_color=ACCENT_LIGHT,
                            icon_size=18,
                            on_click=lambda e: change_goal(1),
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(height=6),
                ft.Row(controls=[goal_bar], spacing=0),
                ft.Container(height=6),
                ft.Row(
                    controls=[goal_done_txt, ft.Container(expand=True), goal_pct_txt],
                ),
            ],
            spacing=4,
        ),
        bgcolor=CARD_COLOR,
        border_radius=14,
        padding=14,
        border=make_border(ACCENT + "40"),
    )

    # ── Qidiruv ─────────────────────────────────────────────
    search_active = [False]

    search_field = ft.TextField(
        hint_text=L("search_hint"),
        hint_style=ft.TextStyle(color=TEXT_SECONDARY),
        color=TEXT_PRIMARY,
        bgcolor=INPUT_BG,
        border_color=DIVIDER_COLOR,
        focused_border_color=ACCENT_LIGHT,
        border_radius=12,
        text_size=14,
        content_padding=12,
        expand=True,
        prefix_icon=ft.Icons.SEARCH_ROUNDED,
        on_change=lambda e: do_search(e.control.value),
    )

    search_clear = ft.IconButton(
        icon=ft.Icons.CLOSE_ROUNDED,
        icon_color=TEXT_SECONDARY,
        icon_size=20,
        visible=False,
        on_click=lambda e: clear_search(),
    )

    search_row = ft.Container(
        content=ft.Row(
            controls=[search_field, search_clear],
            spacing=4,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        visible=False,
        padding=20,
    )

    def do_search(query):
        q = query.strip().lower()
        search_clear.visible = bool(q)
        search_clear.update()
        for task in tasks_list.controls:
            task.visible = (q in task.task_name.lower()) if q else True
            task.update()

    def clear_search():
        search_field.value   = ""
        search_clear.visible = False
        search_field.update()
        search_clear.update()
        for task in tasks_list.controls:
            task.visible = True
            task.update()

    def toggle_search(e):
        search_active[0]     = not search_active[0]
        search_row.visible   = search_active[0]
        search_row.update()
        if search_active[0]:
            search_field.focus()
        else:
            clear_search()



    main_view_container = ft.Container(bgcolor=BG_COLOR, expand=True)

    main_view = ft.Column(
        controls=[header, divider_bar, add_bar, search_row, ft.Divider(color=DIVIDER_COLOR, height=1), tasks_section],
        expand=True, spacing=0, visible=True,
    )
    main_view_container.content = main_view

    page.add(
        ft.Stack(
            controls=[main_view_container, ach_page_container],
            expand=True,
        )
    )

    for item in load_tasks(page):
        loaded_task = Task(
            task_name   = item["name"],
            task_delete = delete_task,
            on_change   = persist,
            created_at  = item.get("created_at", ""),
            is_done     = item.get("is_done", False),
            category    = item.get("category", "Umumiy"),
            priority    = item.get("priority", "Oddiy"),
            due_date    = item.get("due_date"),
            lang        = current_lang[0],
        )
        tasks_list.controls.append(loaded_task)

    goal_placeholder.content = goal_card.content
    goal_placeholder.bgcolor       = goal_card.bgcolor
    goal_placeholder.border_radius = goal_card.border_radius
    goal_placeholder.padding       = goal_card.padding
    goal_placeholder.border        = goal_card.border
    update_counts()
    def refresh_all_text():
        """Til o'zgartirilganda barcha ko'rinadigan matnlarni yangilash"""
        lang = current_lang[0]

        # Sarlavhalar
        ach_title_text.value = t(lang, "achievements_title")

        # Statistika
        level_text.value   = t_level(lang, get_level_index(stats["xp"]))
        update_counts()

        # Filtr tugmalari (matnini yangilaymiz, data kalitlari o'zgarmaydi)
        filter_all_text.value    = t(lang, "filter_all")
        filter_active_text.value = t(lang, "filter_active")
        filter_done_text.value   = t(lang, "filter_done")
        filter_all_text.update()
        filter_active_text.update()
        filter_done_text.update()

        # Add bar
        add_bar_label.value = t(lang, "add_task_btn")
        add_bar_label.update()

        # Forma elementlari
        form_title_text.value = t(lang, "new_task_title")
        form_cat_label.value  = t(lang, "category_label")
        form_pri_label.value  = t(lang, "priority_label")
        form_due_label.value  = t(lang, "due_label")
        form_cancel_text.value = t(lang, "cancel_btn")
        form_add_text.value    = t(lang, "add_btn")
        name_field.hint_text  = t(lang, "task_name_hint")
        due_field.hint_text   = t(lang, "due_not_set")
        form_title_text.update()
        form_cat_label.update()
        form_pri_label.update()
        form_due_label.update()
        form_cancel_btn.update()
        form_add_btn.update()
        name_field.update()
        due_field.update()

        # Dropdown options qayta yaratamiz (kategoriya/muhimlik tarjimasi)
        cat_dropdown.options = [
            ft.dropdown.Option(k, f"{v} {t_cat(lang, k)}") for k, v in CATEGORIES.items()
        ]
        pri_dropdown.options = [
            ft.dropdown.Option(k, f"{v['icon']} {t_pri(lang, k)}") for k, v in PRIORITIES.items()
        ]
        cat_dropdown.update()
        pri_dropdown.update()

        # Qidiruv
        search_field.hint_text = t(lang, "search_hint")
        search_field.update()

        # Kunlik maqsad
        goal_title_text.value = t(lang, "goal_title")
        goal_title_text.update()
        refresh_goal_ui()

        # Barcha vazifa kartalarini joriy tilga moslab qaytadan yaratamiz
        rebuilt = []
        for task in tasks_list.controls:
            new_t = Task(
                task_name=task.task_name,
                task_delete=delete_task,
                on_change=persist,
                created_at=task.created_at,
                is_done=task.is_done,
                category=task.category,
                priority=task.priority,
                due_date=task.due_date,
                lang=lang,
            )
            rebuilt.append(new_t)
        tasks_list.controls = rebuilt

        page.update()

    refresh_stats_ui()
    refresh_goal_ui()
    page.update()


if __name__ == "__main__":
    import asyncio, threading, sys

    async def run_async():
        await ft.app_async(target=main, view=ft.AppView.WEB_BROWSER, port=8550)

    def start_in_thread():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(run_async())
        finally:
            loop.close()

    is_ide = "spyder" in sys.modules or "IPython" in sys.modules

    if is_ide:
        t = threading.Thread(target=start_in_thread, daemon=True)
        t.start()
        print("=" * 45)
        print("  Ilova ishga tushdi!")
        print("  Brauzerda oching: http://localhost:8550")
        print("=" * 45)
    else:
        ft.app(target=main)
