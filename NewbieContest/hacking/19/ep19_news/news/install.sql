# Tables SQL du script NC News

CREATE TABLE `news` (
  `id` int(5) NOT NULL auto_increment,
  `date` varchar(50) NOT NULL default '',
  `pseudo` varchar(50) NOT NULL default '',
  `text` text NOT NULL,
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;

CREATE TABLE `comm_news` (
  `id` int(11) NOT NULL auto_increment,
  `date` varchar(50) NOT NULL default '',
  `auteur` varchar(50) NOT NULL default '',
  `text` text NOT NULL,
  `id_news` int(5) NOT NULL default '0',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;