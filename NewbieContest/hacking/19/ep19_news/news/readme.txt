NC News est un script PHP/MySQL permettant aux webmasters de publier des news en toute
simplicité !

Pour l'installer, rien de plus simple :

- Modifiez le fichier config.php avec vos identifiants SQL
- Importez le fichier install.sql dans PhpMyAdmin
- Uploadez tout le contenu du dossier news sur votre FTP

Pensez à vérifier que le dossier "erreur" dispose de droits écriture (CHMOD 777)

Note : La partie admin n'a pas été codée, la faille ne se situant pas dedans, je n'ai
pas eu le courage de la coder ;)

Pour obtenir le code de validation, il vous faudra parvenir à appeler la fonction validation();
(qui n'est pas codée dans cette version de ce script, mais uniquement sur celle en ligne ;)


