todo:
    1. Criar nova tabela 'campeonato' com informações importantes, como:
        -Numero mínimo e maximo de jogadores por equipe
        -Id usuario organizador
        -estado do campeonato (ORGANIZACAO, ANDAMENTO, ENCERRADO)
        -Numero de equipes esperado
    2. Criar nova tabela 'usuarios' com informações de login:
        -Email
        -senha
        -tipo de usuario (organizador, chefe de equipe, jogador)
    3. Limitar as operações C U D das tabelas baseado no estado do campeonato
        -Equipes só podem ser adicionadas antes do início do campeonato
        -O campeonato só pode ser iniciado com o número esperado de equipes
            -Uma equipe é dita cadastrada quando o número mínimo de jogadores é atingido
        -Jogos só podem ser adicionados durante o andamento. NÃO PODEM SER ALTERADOS.
        -Apenas um resultado pode ser adicionado por jogo. NÃO PODE SER ALTERADO.
        -A classificação será disponível via consumo da tabela resultado
            -Vitória = 1 ponto
            -Critério de desempate: saldo de pontos
            -Empate no caso de dois critérios (pode haver mais de um vencedor)
    4. Limitar os cadastros:
        -Jogadores não podem se cadastrar nas equipes acima do numero de jogadores informado
        -Equipes não podem ter o mesmo nome
        -Apenas uma combinação equipe 1 x equipe 2 é permitida
        -O campeonato acaba imediatamente quando o número de jogos é (n-1)*n/2, onde n-1 é o número de rodadas e n/2 a quantidade de jogos por rodada
