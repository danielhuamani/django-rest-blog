var publicacionColeccion = Backbone.Collection.extend({
	model: publicacionModel,
	url: 'localhost:8000/api/publicaciones/'
})

var publicacion = new publicacionColeccion()

publicacion.fetch();
