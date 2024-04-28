# Teste Backend Amicci

Voce pode ver uma demonstração aqui [Demo](https://test-backend-amicci.onrender.com/api/demo/)

## Instruções

Executar:

### `docker compose up --build`

Ao utilizar esse comando o docker ira criar as migrações, rodar os testes e subir a API seguinte endereço [http://localhost:8000/](http://localhost:8000/)

No endpoint [http://localhost:8000/api/demo/](http://localhost:8000/api/demo/) estará a lista com todas as rotas disponiveis.

## Endpoints

`api/demo/ categories/ [name='category-list-create']`

`api/demo/ category/[int:pk](int:pk)/ [name='category-retrieve-update']`

`api/demo/ vendors/ [name='vendor-list-create']`

`api/demo/ vendor/[int:pk](int:pk)/ [name='vendor-retrieve-update']`

`api/demo/ retailers/ [name='retailer-list-create']`

`api/demo/ retailer/[int:pk](int:pk)/ [name='retailer-retrieve-update']`

`api/demo/ briefings/ [name='briefing-list-create']`

`api/demo/ briefing/[int:pk](int:pk)/ [name='briefing-retrieve-update']`
