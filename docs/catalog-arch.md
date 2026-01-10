# Online Catalog - Architecture Design

## System Flow - Search Request
```mermaid
sequenceDiagram
    participant Client as Angular Frontend
    participant Controller as 10_api/controller<br/>SearchController
    participant DTO as 10_api/dto<br/>ProductDTO
    participant Mapper as 20_application/mapper<br/>ProductMapper
    participant Service as 20_application/service<br/>CatalogService
    participant Repository as 40_infrastructure/repository<br/>ProductRepository
    participant Entity as 30_domain/model<br/>Product
    participant MongoDB as MongoDB

    Note over Client,MongoDB: Search Flow - Clean Architecture (B.1)

    Client->>Controller: GET /api/search?q=motor
    activate Controller
    
    Controller->>Service: searchProducts(query)
    activate Service
    Note over Service: Business logic<br/>Works with ENTITIES
    
    Service->>Repository: findByTitleContaining(query)
    activate Repository
    
    Repository->>MongoDB: Query
    activate MongoDB
    MongoDB-->>Repository: Documents
    deactivate MongoDB
    
    Repository->>Entity: Spring converts<br/>Document → Entity
    activate Entity
    Entity-->>Repository: Product entities
    deactivate Entity
    
    Repository-->>Service: List<Product>
    deactivate Repository
    
    Service-->>Controller: List<Product> entities
    deactivate Service
    
    Note over Controller: Controller does conversion!
    Controller->>Mapper: toDTO(entities)
    activate Mapper
    Mapper->>DTO: creates DTOs
    activate DTO
    DTO-->>Mapper: ProductDTO
    deactivate DTO
    Mapper-->>Controller: List<ProductDTO>
    deactivate Mapper
    
    Controller-->>Client: JSON Response
    deactivate Controller

    Note over Client,MongoDB: Flow: 10_api → 20_application → 30_domain → 40_infrastructure
```

---

# Package Structure (English)
```
backend/src/main/java/catalog/
├── BackendApplication.java
│
├── 10_api/                          # PRESENTATION LAYER
│   ├── controller/                  # HTTP endpoints
│   │   ├── HealthController.java
│   │   └── SearchController.java
│   └── dto/                         # Data Transfer Objects (JSON)
│       ├── ProductDTO.java
│       └── SearchResultDTO.java
│
├── 20_application/                  # APPLICATION LAYER
│   ├── service/                     # Business logic
│   │   └── CatalogService.java
│   └── mapper/                      # Entity ↔ DTO conversion
│       └── ProductMapper.java
│
├── 30_domain/                       # DOMAIN LAYER
│   └── model/                       # Domain entities
│       └── Product.java
│
└── 40_infrastructure/               # INFRASTRUCTURE LAYER
    ├── repository/                  # Data access
    │   └── ProductRepository.java
    └── config/                      # Spring configuration
        └── MongoConfig.java
