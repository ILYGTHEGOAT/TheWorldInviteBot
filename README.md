# 🌍 TheWorldInviteBot

**TheWorldInviteBot** est un bot Discord polyvalent conçu pour générer et envoyer des invitations, avec des fonctionnalités amusantes et un accueil automatique des nouveaux membres. Il permet d'envoyer des liens d’invitation personnalisés, des citations de rap profondes, des blagues, et bien plus encore !


## ✨ Fonctionnalités

- **Invitations sur mesure**  
  - `!invite` : crée une invitation pour le salon actuel (24h, 10 utilisations max) et l’envoie en message privé.  
  - `!invite @utilisateur` : envoie l’invitation à un membre spécifique.  
  - `!invite everyone` : après confirmation, envoie l’invitation à **tous les membres** du serveur (hors bots).

- **Liens permanents personnalisés**  
  - `!winvite` : envoie le lien permanent de **votre serveur** (à configurer).  
  - `!ninvite` : envoie le lien permanent d’**un autre serveur** (à configurer).  
  - Utilisables avec ou sans mention, et aussi en version `everyone`.

- **Accueil automatique**  
  - Quand un nouveau membre rejoint le serveur, le bot lui envoie un message privé avec un lien d’invitation permanent.

- **Commandes amusantes**  
  - `!8ball question` : pose une question à la boule magique.  
  - `!joke` : affiche une blague aléatoire.  
  - `!quote` : affiche une citation profonde issue du rap français.


## 📋 Prérequis

- Python 3.8 ou supérieur
- Un compte Discord et un serveur où vous avez les droits d’ajouter un bot
- Un token de bot Discord (à obtenir sur le [portail développeur Discord](https://discord.com/developers/applications))


## 🚀 Installation

1. **Clonez le dépôt**  
   ```bash
   git clone https://github.com/ILYGTHEGOAT/TheWorldInviteBot.git
   cd TheWorldInviteBot
   ```

2. **Installez les dépendances**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurez le token**  
   - Créez un fichier `.env` à la racine du projet.  
   - Ajoutez-y votre token :
     ```
     DISCORD_TOKEN=VOTRE_TOKEN_ICI
     ```
   - **Ne commitez jamais ce fichier** (il est déjà dans `.gitignore`).

4. **Personnalisez les liens permanents** (optionnel)  
   - Ouvrez `bot.py` et modifiez les variables `FIXED_LINK` dans les commandes `winvite` et `ninvite` avec vos propres liens Discord.

5. **Lancez le bot**  
   ```bash
   python bot.py
   ```


## 🔧 Utilisation

Une fois le bot en ligne et invité sur votre serveur, utilisez les commandes avec le préfixe `!`.

| Commande | Description |
|----------|-------------|
| `!invite` | Crée une invitation et vous l’envoie en MP. |
| `!invite @membre` | Envoie l’invitation au membre mentionné. |
| `!invite everyone` | Envoie l’invitation à tout le serveur (confirmation requise). |
| `!winvite` | Envoie le lien permanent configuré. |
| `!winvite @membre` | Envoie le lien permanent au membre. |
| `!winvite everyone` | Envoie le lien permanent à tout le monde. |
| `!ninvite` | Idem avec un autre lien permanent. |
| `!8ball question` | Réponse magique à votre question. |
| `!joke` | Blague aléatoire. |
| `!quote` | Citation de rap profond. |


## 🤝 Contribuer

Les contributions sont les bienvenues !  
- Signalez un bug ou proposez une amélioration via les [issues GitHub](https://github.com/ILYGTHEGOAT/TheWorldInviteBot/issues).  
- Soumettez une pull request avec des changements clairement décrits.



## 📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de l’utiliser, le modifier et le distribuer, tant que vous conservez la notice de licence.


## 💬 Support

Pour toute question ou assistance, rejoignez mon serveur Discord (lien permanent avec `!winvite`) ou ouvrez une issue sur GitHub.


**Amusez-vous bien avec TheWorldInviteBot !** 🎉
