## Este é um documento para registrar dicas rápidas relacionadas ao Git
 A documentação completa do Git encontra-se [nesse link](https://git-scm.com/doc).<br>
 Uma referência de boas práticas é o [video do Fábio Akita](https://www.youtube.com/watch?v=6OokP-NE49k).<br>
 Outra boa referência é o [curso gratuito no canal do Fabio Ruicci](https://www.youtube.com/playlist?list=PLvS2JoIlSA4DCmp7pbXXuZEUb5E-IDb-K).
<br>
> **`git init`**
> 
>Crie uma nova pasta, abra-a e execute o comando para criar um novo repositório.

> **`git clone <caminho/para/o/repositório>.git`**
>
>Crie uma cópia de trabalho em um repositório local executando o comando.

> **`git commit -m "comentários das alterações"`**
>
>Adicionar comentário ao fazer uma atualização.

> **`git commit -m "comentários das alterações" --amend`** 
>
>Atualiza comentário da última atualização da branch em que se encontra.

> **`git checkout -b <nome_da_funcionalidade>`** 
>
>Crie um novo branch chamado "<funcionalidade_x>" e selecione-o.

> **`git checkout <nome_da_funcionalidade>`** 
>
>Sai da branch atual e vai para a branch <funcionalidade>.

> **`git log --stat`** 
>
>Mostra uma lista dos commits realizados e seus detalhes.

> **`git reset --soft HEAD~3`** 
>
>HEAD - último commit trabalhado
>É possivel voltar até 3 commits anteriores ao atual. O comando remove os commits mas sem descartá-los, possibilitando recuperá-los caso necessário.

> **`git reset --hard HEAD~3`** 
>
>É possivel voltar até 3 commits anteriores ao atual. O comando remove os commits e será impossível recuperá-los.

> **`git branch`** 
>
>Lista todas as branchs locais disponíveis.

> **`git branch -D <nome_da_branch>`** 
>
>A branch local é apagada.

> **`git push origin --delete <branch-name>`**
>
> A branch remota é apagada. A boa prática recomenda executar primeiro a exclusão da branch localmente para, depois executar a exclusão no remoto

> **`git add <nome_da_pasta_ou_arquivo>`** 
>
>Este comando vai adicionar um arquivo ou pasta que devem ser atualizado no repositório.

> **`git add .`** 
>
>Este comando vai adicionar todas as atualizações que foram modificadas.
>Este recurso pode ser perigoso pois pode adicionar arquivos de diferentes contextos.
>Sempre que possível, utilizar o comando anterior.

**<p>-- Sequência de comandos para atualizar a branch atual com as alterações inseridas na develop ou master/main --</p>**
> **`git checkout <develop-ou-master>`**
> Sair da branch da feature em que está trabalhando
> **`git pull`**
> Atualizar o repositório local com as alterações da branch principal
> **`git checkout <feature-branch>`**
> Retornar para a branch da feature que está sendo implementada
> **`git merge <develop-ou-master>`**
> Realizar o merge com a branch principal
> Será aberto o Vim questionano se há a necessidade de resolver conflitos. Resolver se for o caso
> **`git push origin <feature-branch>`**
> Atualizar o repositório remoto com os updates