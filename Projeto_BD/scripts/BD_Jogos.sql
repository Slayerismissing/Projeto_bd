
create table equipes(
	id_equipe serial primary key,
	nome varchar(250) not null,
	regiao varchar(100),
	quant_integrantes integer check (quant_integrantes >= 0)
);

create table jogadores(
	id_jogador serial primary key,
	nome varchar(150) not null,
	regiao varchar(100),
	id_equipe integer not null, 
	constraint fk_equipe_jogador foreign key(id_equipe)
		references equipes(id_equipe)
		on delete restrict
		on update cascade
);

create table jogos(
	id_jogos serial primary key,
	id_equipe1 integer not null,
	id_equipe2 integer not null,
	data_hora timestamp with time zone not null,
	constraint fk_jogos_equipes foreign  key(id_equipe1)
		references equipes(id_equipe)
		on delete restrict
		on update cascade,
	constraint fk_jogos_equipes2 foreign key(id_equipe2)
		references equipes(id_equipe)
		on delete restrict
		on update cascade		
);

create table resultado(
	id_resultado serial primary key,
	id_jogo integer unique not null,
	duracao_partida interval,
	pontos_equipe1 integer,
	pontos_equipe2 integer,
	constraint fk_resultado_jogo foreign key(id_jogo)
		references jogos(id_jogos)
		on delete restrict
		on update cascade
);

create table if not exists task(
	id serial primary key,
	title varchar(255),
	user_id integer,
	foreign key (user_id) references equipes(nome)
);


alter table equipes add column nome_lider varchar(255) not null;

select * from equipes;



