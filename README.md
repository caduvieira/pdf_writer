# Rest PDF Generator

Gera um PDF a partir de parâmetros.

Pode executar com o docker

```shell
docker run --rm -p 80:5000 caduvieira/rest_pdf
```

Depois acesse http://localhost/?cnpj=teste&numero=1

Para validar a hash acesse http://localhost/validar/**hash** 

Exemplo de hash válido http://localhost/validar/41b6b90efc34268fbaae7e142b9ee5412c996d901ec117f090
