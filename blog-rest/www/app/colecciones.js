var app = app || {};
var publicacionColeccion = Backbone.Collection.extend({
	model: publicacionModel,
	url: 'http://104.236.245.239/api/publicaciones/',
	ordenar:'id',

	comparator:function(item){
		return -item.get(this.ordernar);
	}

});

var publicarColeccion = Backbone.Collection.extend({
	model: publicarModel,
	url: 'http://104.236.245.239/api/autores/',
	ordenar:'id',

	comparator:function(item){
		return item.get(this.ordernar);
	}

});

app.publicacionTodas = new publicacionColeccion()
app.publicarTodas = new publicarColeccion()
/*publicacion.fetch();
*/
