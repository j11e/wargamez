NC News est un script PHP/MySQL permettant aux webmasters de publier des news en toute
simplicit� !

Pour l'installer, rien de plus simple :

- Modifiez le fichier config.php avec vos identifiants SQL
- Importez le fichier install.sql dans PhpMyAdmin
- Uploadez tout le contenu du dossier news sur votre FTP

Pensez � v�rifier que le dossier "erreur" dispose de droits �criture (CHMOD 777)

Note : La partie admin n'a pas �t� cod�e, la faille ne se situant pas dedans, je n'ai
pas eu le courage de la coder ;)

Pour obtenir le code de validation, il vous faudra parvenir � appeler la fonction validation();
(qui n'est pas cod�e dans cette version de ce script, mais uniquement sur celle en ligne ;)


