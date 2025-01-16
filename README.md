# Moulinette Minishell

**Une moulinette conçue pour les étudiants de l'école 42, destinée à tester et valider les fonctionnalités du projet Minishell.**

## 📖 Description

Cette moulinette permet de vérifier si les commandes de votre Minishell fonctionnent correctement. Toutefois, en raison de l'interprétation libre du sujet par chaque étudiant, certaines divergences peuvent survenir. Cela peut entraîner des résultats erronés (faux positifs ou négatifs). Vous pouvez personnaliser les tests pour mieux répondre à votre implémentation.

### Points importants :
- **Les bonus ne sont pas pris en compte** : créez vos propres tests pour les bonus ou supprimez ceux d'origine.
- **Contribution encouragée** : améliorez cette moulinette pour aider les futurs étudiants à réussir leur Minishell.

---

## ⚙️ Fonctionnement

La moulinette :
1. Copie votre fichier binaire dans un dossier temporaire.
2. Effectue une série de tests dans cet environnement.
3. Simule diverses entrées utilisateur : texte, flèches, `Ctrl+C`, `Ctrl+D`, signaux, etc.

### 🚀 Lancement

Exécutez la moulinette depuis votre répertoire Minishell :  
```bash
python3 <chemin_de_la_moulinette>/Checker.py [Arguments]
```

---

## 🎨 Configuration du prompt

Si vous utilisez un prompt personnalisé ou coloré, vous devez modifier la fonction `cleanOutput` dans le fichier `DetectNewLine.py`.  
Cette fonction remplace votre prompt par un format standard `@MINISHELL@>`.  

### Exemple :
- **Prompt par défaut** : `minishell$` → aucune modification nécessaire.
- **Prompt personnalisé** : modifiez `cleanOutput` pour refléter votre prompt.

Un exemple est fourni pour les prompts colorés.

---

## 🔧 Options et Arguments

```bash
Usage: python3 Checker.py [all/norme/id_test]
Exemple : python3 Checker.py newline_1
```

### Options disponibles :
- `-d` : Mode debug, affiche les commandes exécutées et les résultats.  
- `-v` : Mode Valgrind, exécute les tests avec Valgrind (⚠️ Attention : certains tests peuvent échouer à cause de modifications du `PATH` par Valgrind).  
- `-e` : Environnement vide, lance les tests sans variables d'environnement (⚠️ déconseillé).  
- `-m=VALUE` : Définit une limite de mémoire (`ulimit -v VALUE`).  
- `-s=VALUE` : Relance les tests à partir d'un ID spécifique.

### Exemples :
```bash
python3 Checker.py -d -v
python3 Checker.py -s=echo_95
python3 Checker.py echo_95
```

⚠️ **Différence entre `-s=ID` et `ID` seul** :
- `-s=ID` : Relance tous les tests à partir de l'ID.
- `ID` : Exécute uniquement le test spécifié.

---

## 🛠️ Tests personnalisés

- **Création et modification** : Vous pouvez créer ou modifier des tests dans le dossier `Tests`.
- **Comparaison** : 
  - Résultats avec `bash --posix` (via `MinishellDiff`).
  - Résultats bruts pour les implémentations sans bonus.

Un fichier contenant 800 tests est inclus (environ 600 tests en réalité, certains ont été supprimés).

---

## 🧪 Vérification de la norme

La moulinette commence par un check de la norme. Si vous souhaitez exclure certains fichiers ou dossiers, modifiez le fichier `Tests/Normes.py` pour personnaliser les règles.

---

## 📌 Remarques

- La moulinette peut échouer si votre ordinateur manque de ressources. Relancez les tests pour vérifier.  
- **Valgrind** :
  - Ignore automatiquement les fuites liées à `readline` et les erreurs `bellow main`.  
  - Utilisez `-d` pour une analyse manuelle avec `-v`.

---

## 💡 Contributions et améliorations

Cette moulinette est susceptible de contenir des défauts. Merci pour votre indulgence et vos retours constructifs. N'hésitez pas à contribuer pour l'améliorer et aider les prochains étudiants !

---

## ✍️ Auteurs

- **Léo Farhi**
- **Pierre Hillebrand**
