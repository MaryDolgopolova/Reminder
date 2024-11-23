from math import remainder
from os import remove
from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import pygame
import time

t = None
music = False  # Переменная для отслеживания проигрывания музыки

def set():
    global t
    rem = sd.askstring("Время напоминания", "Введите время в формате ЧЧ:ММ (24-часовой формат)")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            dt = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            t = dt.timestamp()
            reminder_text = sd.askstring("Текст напоминания", "Введите текст напоминания:")
            label.config(text=f"Напоминание установлено на: {hour:02}:{minute:02}\n  {reminder_text}")
        except ValueError:
            mb.showerror("Ошибка", "Неверный формат времени")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = None
            mb.showinfo("Внимание", "У вас новое напоминание!")
    window.after(10000, check)


def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("Artik.mp3")
    pygame.mixer.music.play()

def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text="Установить новое напоминание")

window = Tk()
window.title("Напоминание")
window.geometry("350x200")
window.iconbitmap (default="reminders_6076.ico")

label = Label(text="Установите напоминание", font=("Comic Sans MS", 14))
label.pack(pady=10)

set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музыку", command=stop_music)
stop_button.pack(pady=5)

check()

window.mainloop()