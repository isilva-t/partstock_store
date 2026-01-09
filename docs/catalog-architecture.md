# Online Catalog - Architecture Design

## System Flow - Search Request
```mermaid
sequenceDiagram
    participant Client as Angular Frontend
    participant Controller as SearchController
    participant Service as CatalogService
    participant Mapper as ProductMapper
    participant Repository as ProductRepository
    participant MongoDB as MongoDB

    Note over Client,MongoDB: Search Flow - Clean Architecture

    Client->>Controller: GET /api/search?q=motor
    activate Controller
    Note over Controller: @RestController<br/>Thin layer - no business logic
    
    Controller->>Service: searchProducts(query)
    activate Service
    Note over Service: Business logic layer<br/>Validates, orchestrates
    
    Service->>Repository: findByTitleContaining(query)
    activate Repository
    Note over Repository: @Repository<br/>Data access only
    
    Repository->>MongoDB: Query documents
    activate MongoDB
    MongoDB-->>Repository: List<Product> entities
    deactivate MongoDB
    
    Repository-->>Service: List<Product>
    deactivate Repository
    
    Service->>Mapper: toDTO(products)
    activate Mapper
    Note over Mapper: Static utility<br/>Entity → DTO conversion
    Mapper-->>Service: List<ProductDTO>
    deactivate Mapper
    
    Service-->>Controller: SearchResultDTO
    deactivate Service
    
    Controller-->>Client: JSON Response
    deactivate Controller

    Note over Client,MongoDB: Separation of Concerns:<br/>Controller → Service → Repository → DB<br/>DTOs for API, Entities for domain
```

## Package Structure
```
src/main/java/com/catalog/
├── controller/      # HTTP Layer - THIN!
├── service/         # Business Logic
├── repository/      # Data Access
├── model/           # Domain Entities
├── dto/             # API DTOs
├── mapper/          # Conversion
└── config/          # Configuration
```
