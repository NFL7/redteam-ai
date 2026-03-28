# Red Team Simulation

## Description
Ce projet simule une **Red Team IA** qui teste la sécurité, la conformité et les risques d’un système cible.  
Le projet inclut des agents simulés pour exécuter différentes tâches et produire des rapports.  
Si le quota OpenAI est dépassé, une fonction hybride simule les réponses des agents.

---

## Agents inclus

| Agent       | Rôle principal                                           | Description détaillée                                         |
|------------|---------------------------------------------------------|---------------------------------------------------------------|
| **Recon**  | Cartographie et identification des failles             | Analyse le système pour détecter les vulnérabilités.        |
| **Attack** | Exécution d’attaques simulées                           | Injecte des attaques fictives pour tester la résilience.    |
| **AI Attack** | Perturbation des décisions prises par l’IA           | Simule une corruption ou manipulation des décisions IA.     |
| **Compliance** | Détection des problèmes de conformité               | Vérifie le respect du RGPD et de l’AI Act.                 |
| **Risk**   | Estimation des impacts financiers et réputationnels    | Évalue les conséquences potentielles des attaques.          |

---

## Installation

1. **Cloner le projet**
```bash
git clone https://github.com/NFL7/redteam-ai.git
cd redteam-ai
