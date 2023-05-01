# tree-menu (древовидное меню)
Тестовое задание компании ООО АпТрейдер (UpTrader) Санкт-Петербург uptrader.io

Task: Develop a Django application to implement a tree-like menu with the following conditions:

The menu should be implemented as a template tag.

All items above the highlighted item should be expanded. The first level of nesting under the highlighted item should also be expanded.

Information about the menu should be stored in a database.

Editing the menu should be done in the standard Django admin panel.

The active menu item should be determined based on the URL of the current page.

There may be multiple menus on one page, which will be displayed based on their names.

Clicking on a menu item should result in navigating to a URL specified in it, which can be specified either explicitly or through a named URL.

Additionally, rendering each menu should be implemented with exactly 1 database query.

To implement the task, a new Django project and application must be created. Inside the application, the MenuItem model must be defined to store information about the menu items and the MenuItemAdminForm form for editing the menu in the admin panel.

To display the menu on the page, a template tag, draw_menu, must be implemented, which will take the name of the menu and return HTML code to display the menu on the page.

All of the above tasks can be implemented using standard Django tools and the standard Python library.

Необходимо разработать Django приложение для реализации древовидного меню согласно следующим условиям:

Меню должно быть реализовано в виде template tag.

Все элементы, которые находятся над выделенным пунктом, должны быть развернуты. Первый уровень вложенности под выделенным пунктом также должен быть развернут.

### Описание задачи на русском языке

Информация о меню должна храниться в базе данных.

Редактирование меню должно производиться в стандартной админке Django.

Активный пункт меню должен определяться на основе URL текущей страницы.

На одной странице может быть несколько меню, которые будут отображаться на основе их названий.

При клике на пункт меню должен происходить переход по заданному URL, который может быть задан явно или через named URL.

Дополнительно, требуется реализовать отрисовку каждого меню с помощью ровно 1 запроса к БД.

Для реализации задачи, необходимо создать новый Django проект и приложение. Внутри приложения необходимо определить модель MenuItem для хранения информации о пунктах меню и форму MenuItemAdminForm для редактирования меню в админке.

Для отображения меню на странице необходимо реализовать шаблонный тег draw_menu, который будет принимать название меню и возвращать HTML-код для отображения меню на странице.

Все вышеперечисленные задачи могут быть реализованы при помощи стандартных инструментов Django и стандартной библиотеки Python.
