var publicacionModel = Backbone.Model.extend({
	urlRoot: 'http://127.0.0.1:8000/api/publicaciones/',
	defaults: {
		titulo: "",
        foto: "",
        contenido: "",
        fecha: "",

	},
	initialize: function(){

		this.on('change:fecha', this.onFecha, this);
	},
	onFecha: function(model){

		var fecha = new Date(model.get('fecha'));
		model.set({fecha:fecha.toString()});
	}
});


var publicarModel = Backbone.Model.extend({
	urlRoot: 'http://127.0.0.1:8000/api/autores/',

});
