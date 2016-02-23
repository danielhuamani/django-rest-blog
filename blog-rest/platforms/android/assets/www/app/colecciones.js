var publicacionColeccion = Backbone.Collection.extend({
	model: publicacionModel,
	url: 'http://104.236.245.239/api/publicaciones/',
	ordenar:'id',

	comparator:function(item){
		return item.get(this.ordernar);
	}

});

var publicacionTodas = new publicacionColeccion()

/*publicacion.fetch();
*/
