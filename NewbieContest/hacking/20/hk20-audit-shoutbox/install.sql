CREATE TABLE `shootbox_admin` (
  `id` mediumint(10) NOT NULL auto_increment,
  `login` varchar(50) NOT NULL default '',
  `password` varchar(35) NOT NULL default '',
  `rank` varchar(10) NOT NULL default '',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
    
CREATE TABLE `shootbox_flood` (
  `now` int(10) NOT NULL default '0',
  `end_flood` int(10) NOT NULL default '0',
  `ip` varchar(50) NOT NULL default ''
) TYPE=MyISAM;

CREATE TABLE `shootbox` (
  `id` mediumint(10) NOT NULL auto_increment,
  `pseudo` varchar(22) NOT NULL default '',
  `email` varchar(50) NOT NULL default '',
  `message` varchar(250) NOT NULL default '',
  `heure` varchar(8) NOT NULL default '',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;