var app = app || {};
app.publicacionesView = Backbone.View.extend({
    el: '#app',
    events:{
        'click .btn-form': 'agregarComentario',
        'click .publicar': 'agregarpublicar',
    },
    agregarpublicar:function(){
        $(".fom-agregar-autor").css("display","block")
        $("#mostrarPublicacion").html('');
        $("#mostrarComentarios").html("");
        $(".form-comentario").css('display', 'none');
        $(".volver-atras").css('display', "block");
        app.publicacionTodas.on('add', this.onAgregarPublicacion);
        app.publicacionTodas.fetch();
    },
    initialize: function(){
        $(".volver-atras").css('display', 'none');
        app.publicacionTodas.on('add', this.onAgregarPublicacion);
        app.publicacionTodas.fetch();
    },
    onAgregarPublicacion: function(modelo, collection, options){
        var publicacion = new mostrarPublicacion({model: modelo});
        $("#mostrarPublicacion").append(publicacion.render().$el)
    },
    agregarComentario: function () {


        app.comentarioTodos.create({
            coment: $('.comentario').val(),
            fk_publicacion: window.idPublicacion,
            usuario: $(".usuario").val(),
        });
        $('.comentario').val('');
        $(".usuario").val('');
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
        $("#mostrarPublicacion").html("")
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

    /*volverAtras:function(){
        console.log("emntr");
        $("#mostrarPublicacion").html('');
    },*/
    initialize: function(){
        $(document).scrollTop(0);
        $(".volver-atras").css('display', 'block');
        $(".form-comentario").css('display', 'block');
        $("#cnt-comentario").html("")
        window.idPublicacion = this.model.get("id");
        var comentarioModel = Backbone.Model.extend({
            urlRoot: "http://127.0.0.1:8000/api/comentarios/"

        })
        /*window.idPublicacion,*/
        var comentarioColeccion = Backbone.Collection.extend({
            model: comentarioModel,
            url: "http://127.0.0.1:8000/api/comentarios/"
        })
        $(".cnt-mostrarComentarios").css("display", "block")
        app.comentarioTodos = new comentarioColeccion();

        app.comentarioTodos.fetch()

        app.comentarioTodos.on("add", this.onAgregarComentario);
        this.model.on("change", this.render, this);
    },

    onAgregarComentario:function(modelo, collection, options){
        var comentario = new mostrarcomentario({model:modelo});

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
        if (this.model.get("fk_publicacion") == window.idPublicacion) {
            this.$el.html(this.template(this.model.toJSON()));
        }
        return this;
    },
})
var appView = new app.publicacionesView();
