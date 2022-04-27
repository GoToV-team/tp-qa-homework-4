# Чек-листы. Patreon
## Команда GoToV
- Варин Дмитрий :sunglasses:
- Ветошкин Артем :blush:
- Ларин Владимир :grinning:
- Нурхаметова Камила :princess:

## Ссылка на проект
[Patreon](https://pyaterochka-team.site/)

## Чек-листы
### Чек-лист №1 (Варин Дмитрий)
#### Вход и редактирование профиля
- [x] Войти в существующий аккаунт
- [x] Изменить фотографию основного профиля
  - Загрузить файл, не являющийся картинкой
  - Загрузить файл, являющийся картинкой 
- [x] Изменить фотографию профиля автора, отличную от фото основного профиля
  - [ ] Загрузить файл, не являющийся картинкой
  - [ ] Загрузить файл, являющийся картинкой 
- [x] Проверить, что фото автора/основного профиля отличаются
- [x] Сменить пароль 
  - Проверить, что изменение пароля валидируется
  - Зайти в аккаунт с новым паролем
  - Сменить на старый пароль
  - Войти снова

### Чек-лист №2 (Ларин Владимир)
#### Добавление поста и редактирование поста
- [ ] Войти в существующий аккаунт автора
- [ ] Нажать кнопку `Панель автора` на странице профиля, который открывается после авторизации
- [ ] Нажать кнопку `Добавить пост`
- [ ] Нажать кнопку `Продолжить`
  - [ ] Убедиться в появлении ошибки валидации
- [ ] Ввести "HELLO WORLD" в текстовое поле `Введите заголовок`
- [ ] Ввести "My description" в текстовое поле `Введите описание`
- [ ] Нажать кнопку `Продолжить`
- [ ] Убедиться в создании черновика поста
  - [ ] Заголовок поста должен быть "HELLO WORLD"
  - [ ] Описание поста должно быть "My description"
  - [ ] У статьи нет загруженных файлов
  - [ ] У статьи нет содержимого
- [ ] Навести мышку на обложку
- [ ] Убедиться в появлении кнопки `Заменить обложку`
- [ ] Нажать на кнопку `Заменить обложку` и загрузить обложку с размером файла больше 20 МБ
- [ ] Убедиться в появлении ошибки загрузки изображения
- [ ] Нажать на кнопку `Заменить обложку` и загрузить обложку записи с размером файла 3 МБ
- [ ] Убедиться в смене картинки обложки изображения на загруженную
  - *Примечание:* качество и размер загруженного на сервер и загруженного с сервера файлов может отличаться, автоматическую проверку реализовать с помощью сравнения короткого имени файла  
- [ ]  Нажать на кнопку `+`
- [ ]  Убедиться в появлении нового блока
- [ ]  Выбрать пустой текстовый блок
- [ ]  Нажать клавишу `Backspace`
- [ ]  Убедиться в удалении данного пустого блока
- [ ]  Нажать на иконку ноты
- [ ]  Убедиться в появлении блока `Загрузить аудио`.
- [ ]  Нажать на блок `Загрузить аудио` и загрузить невалидный файла (валидным считается, файл расширения `.ogg`, `.mp3` не более 20 МБ)
- [ ]  Убедиться в появлении ошибки валидации/загрузки
- [ ]  Нажать на блок `Загрузить аудио` и загрузить валидный файла (валидным считается, файл расширения `.ogg`, `.mp3` не более 20 МБ)
- [ ] Убедиться в загрузке файла
- [ ] Нажать на иконку изображения в пустом блоке
- [ ] Убедиться в появлении блока загрузки изображения.
- [ ] Нажать на блок `Заменить изображение` и загрузить невалидный файл (валидным считается, файл расширения `.png`, `.jpg` не более 20 МБ) 
- [ ] Убедиться в появлении ошибки загрузки
- [ ] Нажать на блок `Заменить изображение` и загрузить валидный файл (валидным считается, файл расширения `.png`, `.jpg` не более 20 МБ) 
- [ ] Убедиться в появлении загруженного изображения
- [ ] Нажать на иконку видео-пленки 
- [ ] Убедиться в появлении блока `Загрузить видео`.
- [ ] Нажать на блок `Загрузить видео`. Загрузить невалидный файла (валидным считается, файл с mime-типом `video/mp4` ,`video/mpeg` ,`video/mpeg4-generic` не более 100 МБ)
- [ ] Убедиться в появлении сообщения об ошибке.
- [ ] Нажать на блок `Загрузить видео`. Загрузить валидный файла (валидным считается, файл с mime-типом `video/mp4` ,`video/mpeg` ,`video/mpeg4-generic` не более 100 МБ)
- [ ] Убедиться в загрузке видео.
- [ ] Ввести текст "THIS TEXT" в пустой текстовый блок
- [ ] Убедиться, что иконки аудио, изображения и видео меняются на иконку корзины.
- [ ] Нажать на кнопку `Сохранить`
- [ ] Убедиться в появлении страницы поста, на странице поста должны присутствовать 
    - [] загруженной обложки
    - [] загруженного изображения
    - [] загруженного видео
    - [] текстового блока "THIS TEXT"
- [ ] Нажать кнопку `Редактировать`
- [ ] Убедиться в присутствии на странице
  - [ ] загруженной обложки
  - [ ] загруженного изображения
  - [ ] загруженного видео
  - [ ] текстового блока "THIS TEXT"
- [ ] Нажать на кнопку `удалить`
- [ ] Убедиться в появлении предупреждение об удалении.
- [ ] Нажать кнопку `Отмена`
- [ ] Убедиться в сохранении на странице загруженных обложки, изображения, видео и введенного текстового блока "THIS TEXT"
- [ ] Нажать на кнопку `удалить`
- [ ] Нажать на кнопку `удалить`
- [ ] убедиться в переходе в панель автора
- [ ] убедиться в отсутствии поста "HELLO WORLD" в списке постов

### Чек-лист №3 (Ветошкин Артем)
#### Добавление уровня и редактирование уровня
- [ ] Войти в существующий аккаунт автора
- [ ] Нажать кнопку `Настройки` в выпадающем меню пользователя
- [ ] Выбрать вкладку `Аккаунт автора`
- [ ] Нажать на иконку `Добавить уровень подписки`
  - [ ] Убедиться в появлении ошибки валидации
- [ ] Ввести "Первый уровень" в текстовое поле `Название уровня`
- [ ] Ввести "Хорошее преимущество" в текстовое поле `Название преимущества`
- [ ] Нажать на кнопку `Заменить обложку` и загрузить обложку с размером файла больше 20 МБ
- [ ] Убедиться в появлении ошибки загрузки изображения
- [ ] Нажать на кнопку `Заменить обложку` и загрузить обложку записи с размером файла 3 МБ
- [ ] Убедиться в смене картинки обложки изображения на загруженную
- [ ] Нажать на кнопку `Добавить преимущество`
- [ ] Убедиться в появлении дополнительного поля `Название преимущества`
- [ ] Ввести "Второе хорошее преимущество" в текстовое поле `Название преимущества`
- [ ] Ввести "Привет мир" в текстовое поле `Стоимость подписки в месяц, рубли`
- [ ] Убедиться в появлении ошибки об некоректном значении поля
- [ ] Заменить текст в поле `Стоимость подписки в месяц, рубли` на "20"
- [ ] Убедиться в работе предпросмотра уровня
  - [ ] Заголовок карточки должен быть "Первый уровень"
  - [ ] Первое преимущество в карточке должно быть "Хорошее преимущество"
  - [ ] Второе преимущество в карточке должно быть "Второе хорошее преимущество"
  - [ ] Цена уровня подписки должна быть "20"
- [ ] Нажать кнопку `Сохранить`
- [ ] Убедиться в появлении уровня в списке уровней подписки
  - [ ] Заголовок карточки должен быть "Первый уровень"
  - [ ] Первое преимущество в карточке должно быть "Хорошее преимущество"
  - [ ] Второе преимущество в карточке должно быть "Второе хорошее преимущество"
  - [ ] Цена уровня подписки должна быть "20"
- [ ] Нажать кнопку `Редактировать уровень`
- [ ] Ввести "Редактированный уровень" в текстовое поле `Название уровня`
- [ ] Ввести "Редактированное преимущество" в первое текстовое поле `Название преимущества`
- [ ] Нажать на иконку крестика во второе текстовое поле `Название преимущества`
- [ ] Убедиться в исчезновении второго текстового поля `Название преимущества`
- [ ] Нажать на кнопку `Заменить обложку` и загрузить обложку с размером файла больше 20 МБ
- [ ] Убедиться в появлении ошибки загрузки изображения
- [ ] Нажать на кнопку `Заменить обложку` и загрузить обложку записи с размером файла 3 МБ
- [ ] Убедиться в смене картинки обложки изображения на загруженную
- [ ] Нажать на кнопку `Добавить преимущество`
- [ ] Убедиться в появлении дополнительного поля `Название преимущества`
- [ ] Ввести "Третье редактированное преимущество" во новое текстовое поле `Название преимущества`
- [ ] Ввести "Привет мир" в текстовое поле `Стоимость подписки в месяц, рубли`
- [ ] Убедиться в появлении ошибки об некоректном значении поля
- [ ] Заменить текст в поле `Стоимость подписки в месяц, рубли` на "30"
- [ ] Убедиться в работе предпросмотра уровня
  - [ ] Заголовок карточки должен быть "Редактированный уровень"
  - [ ] Первое преимущество в карточке должно быть "Редактированное преимущество"
  - [ ] Второе преимущество в карточке должно быть "Третье редактированное преимущество"
  - [ ] Цена уровня подписки должна быть "30"
- [ ] Нажать кнопку `Сохранить`
- [ ] Убедиться в извенение уровня в списке уровней подписки
  - [ ] Заголовок карточки должен быть "Редактированный уровень"
  - [ ] Первое преимущество в карточке должно быть "Редактированное преимущество"
  - [ ] Второе преимущество в карточке должно быть "Третье редактированное преимущество"
  - [ ] Цена уровня подписки должна быть "30"
- [ ] Нажать кнопку `Редактировать уровень`
- [ ] Нажать кнопку `Удалить`
- [ ] Нажать кнопку `Отменить`
- [ ] Нажать кнопку `Сохранить`
- [ ] Убедиться в неизменности уровня в списке уровней подписки
  - [ ] Заголовок карточки должен быть "Редактированный уровень"
  - [ ] Первое преимущество в карточке должно быть "Редактированное преимущество"
  - [ ] Второе преимущество в карточке должно быть "Третье редактированное преимущество"
  - [ ] Цена уровня подписки должна быть "30"
- [ ] Нажать кнопку `Редактировать уровень`
- [ ] Нажать кнопку `Удалить`
- [ ] Нажать кнопку `Удалить`
- [ ] Убедиться в отсутсвии уровня в списке уровней подписки
