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

> **`git log`** 
>
>Mostra uma lista dos commits realizados e seus detalhes.

> **`git reset --soft HEAD~3`** 
>
>HEAD - último commit trabalhado
>É possivel voltar até 3 commits anteriores ao atual. O comando remove os commits mas sem descartá-los, possibilitando recuperá-los caso necessário.

> **`git reset --hard HEAD~3`** 
>
>É possivel voltar até 3 commits anteriores ao atual. O comando remove os commits e será impossível recuperá-los.