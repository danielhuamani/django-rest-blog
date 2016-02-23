var publicacionesView = Backbone.View.extend({
	el: '#app',
	initialize: function(){
		/*$(".volver-atras").css('display', 'none');*/
		publicacionTodas.on('add', this.onAgregarPublicacion);
		publicacionTodas.fetch();
	},
	onAgregarPublicacion: function(modelo, collection, options){
		var publicacion = new mostrarPublicacion({model: modelo});
		$("#mostrarPublicacion").append(publicacion.render().$el)
	}
});

var mostrarPublicacion = Backbone.View.extend({
	template: _.template($("#templatePublicacion").html()),
	events:{
		'click .btn-ver-mas': 'verDetalle',
		/*'click .volver-atras': 'volverAtras',*/
	},
	/*volverAtras:function(){
		console.log("emntr");
		$("#mostrarPublicacion").html('');
	},*/
	verDetalle:function(){
		$("#mostrarPublicacion").html('');
		this.model.fetch();
		var detallepublicacion = new detallePublicacion({model:this.model})

		$("#mostrarPublicacion").append(detallepublicacion.render().$el)
	},
	render: function(){
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

var detallePublicacion = Backbone.View.extend({

	template: _.template($("#templatePublicacionDetalle").html()),

	initialize: function(){
		/*$(".volver-atras").css('display', 'block');*/
		$(".form-comentario").css('display', 'block');
		$("#cnt-comentario").html("")
		window.idPublicacion = this.model.get("id");
		var comentarioModel = Backbone.Model.extend({
			urlRoot: "http://104.236.245.239/api/publicaciones/"+window.idPublicacion
		})
		var comentarioColeccion = Backbone.Collection.extend({
			model: comentarioModel,
			url: "http://104.236.245.239/api/publicaciones/"+window.idPublicacion,
		})
		var comentarioTodos = new comentarioColeccion();
		comentarioTodos.fetch()
		comentarioTodos.on("add", this.onAgregarComentario);
		this.model.on("change", this.render, this);
	},
	onAgregarComentario:function(modelo, collection, options){
		var comentario = new mostrarcomentario({model:modelo});
		console.log(comentario)
		$("#mostrarComentarios").append(comentario.render().$el)
	},
	render: function(){

		this.$el.html(this.template(this.model.toJSON()));
		return this;
	},
})

var mostrarcomentario = Backbone.View.extend({
	template: _.template($("#tempalteComentario").html()),
	render: function(){

		this.$el.html(this.template(this.model.toJSON()));
		return this;
	},
})
var appView = new publicacionesView();
