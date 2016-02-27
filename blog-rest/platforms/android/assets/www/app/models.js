var publicacionModel = Backbone.Model.extend({
	urlRoot: 'http://104.236.245.239/api/publicaciones/',
	defaults: {
		titulo: "",
        foto: "",
        contenido: "",
        fecha: "",
        fecha_cort: "",

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
	urlRoot: 'http://104.236.245.239/api/autores/',

});
