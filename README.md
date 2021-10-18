# Projeto para o curso em MOOC - Programmer l'internet des objets
## Projeto criado a partir dos conceitos aprendidos no curso de IOT, o curso em francês consistiu em utilizar um laboratório virtual em ambiente Linux. Aqui tento relatar um pouco do que aprendi utilizando outras formas de implementação.
### Noções básicas de Internet das Coisas
Na primeira semana como atividade prática, o Wireshark foi utilizado para analisar quadros HTTP, assim como controlar um objeto distante com o protocolo MODBUS.
### Estruturação compacta dos dados
Nesta seção vimos como os dados transportados são estruturados na Internet das Coisas. Vimos a serialização dos dados. Como meio de economia de energia utiliza-se formatos como JSON e CBOR.
### Transporte de Dados
Nesta seção, a exploração de dados foi um pouco mais adiante ao se estudar um pouco da arquitetura de software REST e o protocolo CoAP. 
### Informações semânticas
Vimos que não são apenas os dados que constituem a informação, mas também o significado deles. Um diagrama de classes UML foi utilizado para modelar e especificar uma ontologia, representando um conjunto de conceitos dentro de um domínio e os relacionamentos entre estes. A fim de formalizar esse modelo UML foi utilizado o JSON. Por fim, como atividade prática os dados foram armazenados em um banco de dados MongoDB no fomato JSON.
### Rumo a exploração de dados
A análise dos dados permite reconhecer possíveis distorções que podem aparecer na série de dados associados ao sensor durante o monitoramento. Observamos através de um modelo matemático o valor medido e o valor real. O bias (viés) que é visto como um desvio de veracidade. Além do bias temos o ruído que consiste no que podemos chamar de desvio de fidelidade porque se trata de um ruído de medição e é visto no modelo matemático como um desvio padrão. Por fim, a qualidade dos dados deve ser avaliada antes de qualquer uso dos dados, quer seja controle, supervisão, previsão ou diagnóstico. Se os dados possuem qualidade suficiente eles podem partir para a próxima etapa que é a Inteligência Artificial.
