### cross site request forgery
    flask alredy takes care of this, but we have to
    create a secret key using the app.config so flask can
    generate a token that will be used to track the authenticity
    of a requet that is sent from the user.
