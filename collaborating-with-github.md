# Collaborating on an Omniverse Project with GitHub

In this tutorial your group sets up one shared Omniverse project on GitHub. Each person builds their part in their **own USD layer**, GitHub keeps everyone's copy in sync, and one **main scene** combines all the layers into a single world.

You don't need to write code. Everything is done in **GitHub Desktop** and **USD Composer**.

## How it works

```
group01-project/
├── main.usda                 ← the combined scene: holds the layers, nothing else
├── layers/
│   ├── environment_ana.usda  ← one layer per student
│   ├── lighting_sam.usda
│   └── props_lee.usda
├── assets/                   ← models and textures the group uses
├── data/                     ← CSV datasets
└── scripts/                  ← data connection scripts
```

- **`main.usda`** is the group's world. It doesn't contain objects itself; it pulls in everyone's layers.
- **Each student edits only their own layer.** Because no two people save the same file, nobody overwrites anyone else's work.
- **GitHub** stores the project online. You **pull** to get your teammates' work and **push** to share yours.

> **Why layers?** A USD layer is a file of changes stacked on top of a scene. Layers let several people contribute to one world without touching each other's files. It's the same idea as layers in Photoshop, applied to 3D.

## What you need

- A **GitHub account**. Sign up at [github.com](https://github.com) with your ASU email.
- **GitHub Desktop**, from [desktop.github.com](https://desktop.github.com). Sign in with your GitHub account after installing.
- **USD Composer**, the Omniverse app you already use in class.
- The **starter kit** from your instructor (`starter-kit.zip`).

**Roles:** one person in each group is the **group lead**. The lead does Part 1. Everyone does Part 2 onwards.

---

## Part 1: Create the repository (group lead only)

### Step 1: Create the repository on GitHub

1. Go to [github.com](https://github.com) and click **New** (or the **+** menu at the top right → **New repository**).
2. Fill in:
   - **Owner:** the class organization (for example `ASU-IXD`), if your instructor has added you to it. Otherwise, your own account.
   - **Repository name:** your group's name, for example `group01-project`. Use lowercase letters and dashes only.
   - **Visibility:** **Private**.
   - Tick **Add a README file**.
3. Click **Create repository**.

### Step 2: Invite your group

1. In the new repository, open **Settings → Collaborators** (called **Collaborators and teams** in an organization).
2. Click **Add people** and add each teammate's GitHub username, plus your instructor. Give them **Write** access if asked.
3. Teammates get an email invitation and must click **Accept** before they can work.

### Step 3: Copy the repository to your computer

1. Open **GitHub Desktop**.
2. **File → Clone repository**, choose your new repository from the list, and set the **Local path**. Use a short path without spaces, for example `C:\omniverse\projects\group01-project`.
3. Click **Clone**.

### Step 4: Add the starter kit

1. Unzip **`starter-kit.zip`**.
2. Copy **everything inside it** into your repository folder: `.gitattributes`, `.gitignore`, `README.md` (replace the existing one), and the folders `layers`, `assets`, `data` and `scripts`.

   > `.gitattributes` and `.gitignore` start with a dot, so Windows may hide them. In File Explorer, turn on **View → Show → Hidden items** to check they were copied.

3. Open `README.md` in any text editor and fill in your group name, project title and team table.

What the two settings files do:
- **`.gitattributes`** tells Git to store large files (models, textures, videos) with **Git LFS** (Large File Storage). Without it, GitHub rejects or struggles with big 3D files.
- **`.gitignore`** keeps temporary files out of the project.

### Step 5: Build the main scene and one layer per person

1. Open **USD Composer** and choose **File → New**.
2. **File → Save As**, save into the repository folder, and name it **`main.usda`**. Make sure the file type is `.usda`.
3. Open the **Layer** panel (**Window → Layer** if it isn't showing).
4. For each person in the group, including yourself:
   - Click **Create Sublayer** in the Layer panel.
   - Save it in the **`layers`** folder as **`[part]_[name].usda`**, for example `lighting_sam.usda`.
5. You should now see `main.usda` at the top of the Layer panel, with one sublayer per person under it.
6. **File → Save** to save `main.usda`.

> **Check:** every file must be inside your repository folder. A layer saved anywhere else won't reach your teammates.

### Step 6: Share it (your first commit and push)

1. Switch to **GitHub Desktop**. The left panel lists everything you added.
2. If GitHub Desktop asks to **initialize Git LFS**, click **Initialize Git LFS**.
3. At the bottom left, type a **summary**, for example `Set up project structure and layers`.
4. Click **Commit to main**.
5. Click **Push origin** at the top.

Open the repository on github.com and refresh. You should see `main.usda`, the `layers` folder with everyone's layer, and the other folders.

**Part 1 is done.** Tell your group they can start.

---

## Part 2: Join the project (everyone)

### Step 7: Accept the invitation and clone

1. Accept the GitHub invitation from your email (or from **github.com → your profile → notifications**).
2. In **GitHub Desktop**: **File → Clone repository**, pick your group's repository, and set the **Local path**. Use the same path as your teammates if you can, for example `C:\omniverse\projects\group01-project`.
3. Click **Clone**.

### Step 8: Open the project and find your layer

1. In **USD Composer**, open **`main.usda`** from your repository folder.
2. In the **Layer** panel, find **your** layer, the one with your name.

**Part 2 is done.** You're ready to work.

---

## Part 3: The everyday workflow (every session)

Every time you work on the project, follow these six steps in order.

### Step 9: Pull first

In **GitHub Desktop**, click **Fetch origin**. If it changes to **Pull origin**, click it. You now have everyone's latest work.

> **Always pull before you open the scene.** Working on an old copy is the main cause of problems.

### Step 10: Open the scene

Open **`main.usda`** in USD Composer. If it was already open, close it and open it again so you see your teammates' latest changes.

### Step 11: Set YOUR layer as the edit target

In the **Layer** panel, make **your layer** the one you're editing: **double-click it** (or right-click → **Set Authoring Layer**). Your layer is highlighted as the active, authoring layer.

> **This is the most important step.** Whatever you change goes into the layer that's set here. If you skip it, your work lands in `main.usda` or in a teammate's file.

### Step 12: Build

Work as you normally do: add objects, lights and materials, animate, and run data scripts. Two habits keep things clean:

- **Put your objects in your own group.** Create an **Xform** under `/World` named after you (for example `/World/Sam`) and build inside it. Then your objects never clash with a teammate's.
- **Save new models and textures in the `assets` folder** of the repository before adding them to the scene, so your teammates have them too.

### Step 13: Save

**File → Save.** Only your layer should be saved.

### Step 14: Commit and push

1. Switch to **GitHub Desktop** and look at the **changed files** list on the left.
2. **Check it:** you should only see **your layer** and any **assets or data files you added**.
   - If **`main.usda`** or a **teammate's layer** appears, don't commit it. Right-click it → **Discard changes**. Then check Step 11 next time.
3. Write a short **summary** of what you did, for example `Added lamp and temperature-driven lights`.
4. Click **Commit to main**, then **Push origin**.

Your teammates see your work the next time they pull.

---

## Rules for the group

1. **Pull before you start, push when you finish.**
2. **Edit only your own layer.** Only the group lead changes `main.usda`, for example to add a layer for a new member.
3. **Check the changed files before every commit.** Only your files should be there.
4. **Put shared files in the repository folders:** models and textures in `assets`, CSVs in `data`, scripts in `scripts`.
5. **One owner per model.** Two people editing the same model file can't be merged, so one person's version is lost.
6. **Write clear commit summaries**, so the group can see who changed what.

---

## Things that commonly go wrong

| Problem | Why it happens | Fix |
| --- | --- | --- |
| `main.usda` or a teammate's layer shows in your changes | You edited without setting your own layer as the target (Step 11) | Right-click those files in GitHub Desktop → **Discard changes** |
| A teammate's work doesn't appear | You didn't pull, or the scene was already open | **Pull**, then close and reopen `main.usda` |
| Pink or missing textures or models on a teammate's computer | The file was saved outside the repository, or referenced with a full path such as `C:\Users\...` | Move the file into `assets`, then re-add it from there. In **Properties → References**, the path should start with `./` or `../` |
| GitHub Desktop says "push rejected" | A teammate pushed while you were working | Click **Pull origin**, then **Push origin** again |
| GitHub Desktop shows a **conflict** | Two people changed the same file | For a teammate's file, keep **their** version. For a shared file, talk to the group lead before choosing |
| GitHub refuses a file over 100 MB | GitHub's maximum file size | Reduce the model or texture size, or split it up |
| A data script can't find its CSV | The script points to a folder outside the repository | Set the script's data path to your repository's `data` folder |

---

## Reviewing the combined world

To show the group's work in class, one computer **pulls the latest version** and opens `main.usda`, either in USD Composer or in the **USD Viewer streaming app**, so others can watch in a browser. Everyone's layers appear together as one world.

---

## For instructors

- **Make the starter kit a template repository.** Create one repository with the starter kit, then turn on **Settings → Template repository**. Groups can click **Use this template** to create their own copy, which replaces Steps 1 and 4.
- **Storage limits.** GitHub blocks single files over 100 MB, and Git LFS storage and bandwidth are limited on free accounts. Check the class organization's LFS usage under **Settings → Billing** before deadlines, and check whether GitHub Education gives the organization more.
- **A suggested class flow:** Part 1 as a live demo (about 20 minutes), then groups do Part 2 and one full loop of Part 3 together (about 30 minutes). End with each student pushing one small change and everyone pulling to see the combined world.
