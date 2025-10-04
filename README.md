# DogSense – Auto Repo (One-Click-ish)

**מוכן לקוד-אום/קודקס/קודספייסס ול-Mac בלחיצה.**

## 1) שימוש ב-GitHub Codespaces (הכי אוטומטי)
- פתח את הריפו הזה כ-Codespace. קובץ `.devcontainer/devcontainer.json` יריץ אוטומטית:
  - `bash setup.sh` (סביבה ותלויות)
  - `python scripts/analyze_annotations.py` (יקרא `annotations.csv` אם קיים, אחרת `sample_annotations.csv`).
- כדי להשתמש בדאטה שלך: העלה קובץ בשם **`annotations.csv`** לשורש הריפו ופתח מחדש/הריץ `bash run.sh`.

## 2) שימוש מקומי ב-Mac (כפתור אחד)
- שים את `annotations.csv` בשורש התיקייה (או השתמש ב-`sample_annotations.csv`).
- לחץ פעמיים על: **Run_Pipeline_Mac.command**
- בסוף יווצרו קבצים: `splits/train.csv`, `splits/val.csv`, `splits/test.csv`.

## 3) Notebook
- הפעל `notebook.sh` או פתח את `notebooks/DogSense_Data_Prep.ipynb` ב-VS Code/Notebook.

## מבנה קלט צפוי (CSV)
עמודות חובה: `video_id,file_name,subject,behavior,start_time_sec,end_time_sec,result,feedback_type`

בהצלחה! 🐶📈
