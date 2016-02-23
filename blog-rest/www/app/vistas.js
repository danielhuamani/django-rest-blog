var publicacionesView = Backbone.View.extend({
	el: '#app',
	initialize: function(){
		publicacionTodas.on('add', this.onAgregarPublicacion);
		publicacionTodas.fetch();
	},
	onAgregarPublicacion: function(modelo, collection, options){
		console.log(modelo);
		var publicacion = new mostrarPublicacion({model: modelo});
		$("#mostrarPublicacion").append(publicacion.render().$el)
	}
});

var mostrarPublicacion = Backbone.View.extend({
	template: _.template($("#templatePublicacion").html()),
	render: function(){
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

var appView = new publicacionesView();
