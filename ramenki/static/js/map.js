  ymaps.ready(function () {
    var map01 = new ymaps.Map('map-01', {
          center: [55.81242269713803,37.6634309090728],
          zoom: 11
      }
      // , {
      //     searchControlProvider: 'yandex#search'
      // }
      ),

    placemark01_01 = new ymaps.Placemark([55.71242269,37.6634309],
    {
        hintContent: 'Главный Додзё',
        balloonContent: 'Главный Додзё'
    }, {
        // Опции.
        // Необходимо указать данный тип макета.
        iconLayout: 'default#image',
        // Своё изображение иконки метки.
        iconImageHref: 'img/map-point.png',
        // Размеры метки.
        iconImageSize: [106, 111],
        // Смещение левого верхнего угла иконки относительно
        // её "ножки" (точки привязки).
        iconImageOffset: [-53, -111]
    }),

    placemark01_02 = new ymaps.Placemark([55.81242269713803,37.6734309],
    {
        hintContent: 'Главный Додзё',
        balloonContent: 'Главный Додзё'
    }, {
        // Опции.
        // Необходимо указать данный тип макета.
        iconLayout: 'default#image',
        // Своё изображение иконки метки.
        iconImageHref: 'img/map-point.png',
        // Размеры метки.
        iconImageSize: [106, 111],
        // Смещение левого верхнего угла иконки относительно
        // её "ножки" (точки привязки).
        iconImageOffset: [-53, -111]
    });

    map01.geoObjects
      .add(placemark01_01)
      .add(placemark01_02);

    var map02 = new ymaps.Map('map-02', {
        center: [51.66908885130271,39.186609602050765],
        zoom: 11
      }
      // , {
      //     searchControlProvider: 'yandex#search'
      // }
      ),

    placemark02_01 = new ymaps.Placemark([51.689,39.03],
    {
        hintContent: 'Главный Додзё',
        balloonContent: 'Главный Додзё'
    }, {
        // Опции.
        // Необходимо указать данный тип макета.
        iconLayout: 'default#image',
        // Своё изображение иконки метки.
        iconImageHref: 'img/map-point.png',
        // Размеры метки.
        iconImageSize: [106, 111],
        // Смещение левого верхнего угла иконки относительно
        // её "ножки" (точки привязки).
        iconImageOffset: [-53, -111]
    });

    map02.geoObjects
      .add(placemark02_01);



  });


