from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Domain.Entities.Usuarios import base_usuarios
from Domain.Entities.Administradores import base_administradores
from Domain.Entities.Aulas import base_aulas
from Domain.Entities.AvaliacoesCursos import base_avaliacoes_cursos
from Domain.Entities.Cursos import base_cursos
from Domain.Entities.CursosFavoritos import base_cursos_favoritos

DATABASE_URL = "sqlite:///cursosdb.db"
engine = create_engine(DATABASE_URL, echo=False)

### Migration
base_usuarios.metadata.create_all(bind=engine)
base_administradores.metadata.create_all(bind=engine)
base_aulas.metadata.create_all(bind=engine)
base_avaliacoes_cursos.metadata.create_all(bind=engine)
base_cursos.metadata.create_all(bind=engine)
base_cursos_favoritos.metadata.create_all(bind=engine)

#Context Banco
dbcursos = sessionmaker(autocommit=False, autoflush=False, bind=engine)


