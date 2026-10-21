# hook_menu()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1264–1279 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1264-L1279)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_menu()
```

## Documentation

```text
Define menu items and page callbacks.

This hook enables modules to register paths in order to define how URL
requests are handled. Paths may be registered for URL handling only, or they
can register a link to be placed in a menu (usually the Navigation menu). A
path and its associated information is commonly called a "menu router item".
This hook is rarely called (for example, when modules are enabled), and
its results are cached in the database.

hook_menu() implementations return an associative array whose keys define
paths and whose values are an associative array of properties for each
path. (The complete list of properties is in the return value section below.)

@section sec_callback_funcs Callback Functions
The definition for each path may include a page callback function, which is
invoked when the registered path is requested. If there is no other
registered path that fits the requested path better, any further path
components are passed to the callback function. For example, your module
could register path 'abc/def':
@code
  function mymodule_menu() {
    $items['abc/def'] = array(
      'page callback' => 'mymodule_abc_view',
    );
    return $items;
  }

  function mymodule_abc_view($ghi = 0, $jkl = '') {
    // ...
  }
@endcode
When path 'abc/def' is requested, no further path components are in the
request, and no additional arguments are passed to the callback function (so
$ghi and $jkl would take the default values as defined in the function
signature). When 'abc/def/123/foo' is requested, $ghi will be '123' and
$jkl will be 'foo'. Note that this automatic passing of optional path
arguments applies only to page and theme callback functions.

@subsection sub_callback_arguments Callback Arguments
In addition to optional path arguments, the page callback and other callback
functions may specify argument lists as arrays. These argument lists may
contain both fixed/hard-coded argument values and integers that correspond
to path components. When integers are used and the callback function is
called, the corresponding path components will be substituted for the
integers. That is, the integer 0 in an argument list will be replaced with
the first path component, integer 1 with the second, and so on (path
components are numbered starting from zero). To pass an integer without it
being replaced with its respective path component, use the string value of
the integer (e.g., '1') as the argument value. This substitution feature
allows you to re-use a callback function for several different paths. For
example:
@code
  function mymodule_menu() {
    $items['abc/def'] = array(
      'page callback' => 'mymodule_abc_view',
      'page arguments' => array(1, 'foo'),
    );
    return $items;
  }
@endcode
When path 'abc/def' is requested, the page callback function will get 'def'
as the first argument and (always) 'foo' as the second argument.

If a page callback function uses an argument list array, and its path is
requested with optional path arguments, then the list array's arguments are
passed to the callback function first, followed by the optional path
arguments. Using the above example, when path 'abc/def/bar/baz' is requested,
mymodule_abc_view() will be called with 'def', 'foo', 'bar' and 'baz' as
arguments, in that order.

Special care should be taken for the page callback drupal_get_form(), because
your specific form callback function will always receive $form and
&$form_state as the first function arguments:
@code
  function mymodule_abc_form($form, &$form_state) {
    // ...
    return $form;
  }
@endcode
See @link form_api Form API documentation @endlink for details.

@section sec_path_wildcards Wildcards in Paths
@subsection sub_simple_wildcards Simple Wildcards
Wildcards within paths also work with integer substitution. For example,
your module could register path 'my-module/%/edit':
@code
  $items['my-module/%/edit'] = array(
    'page callback' => 'mymodule_abc_edit',
    'page arguments' => array(1),
  );
@endcode
When path 'my-module/foo/edit' is requested, integer 1 will be replaced
with 'foo' and passed to the callback function. Note that wildcards may not
be used as the first component.

@subsection sub_autoload_wildcards Auto-Loader Wildcards
Registered paths may also contain special "auto-loader" wildcard components
in the form of '%mymodule_abc', where the '%' part means that this path
component is a wildcard, and the 'mymodule_abc' part defines the prefix for a
load function, which here would be named mymodule_abc_load(). When a matching
path is requested, your load function will receive as its first argument the
path component in the position of the wildcard; load functions may also be
passed additional arguments (see "load arguments" in the return value
section below). For example, your module could register path
'my-module/%mymodule_abc/edit':
@code
  $items['my-module/%mymodule_abc/edit'] = array(
    'page callback' => 'mymodule_abc_edit',
    'page arguments' => array(1),
  );
@endcode
When path 'my-module/123/edit' is requested, your load function
mymodule_abc_load() will be invoked with the argument '123', and should
load and return an "abc" object with internal id 123:
@code
  function mymodule_abc_load($abc_id) {
    return db_query("SELECT * FROM {mymodule_abc} WHERE abc_id = :abc_id", array(':abc_id' => $abc_id))->fetchObject();
  }
@endcode
This 'abc' object will then be passed into the callback functions defined
for the menu item, such as the page callback function mymodule_abc_edit()
to replace the integer 1 in the argument array. Note that a load function
should return FALSE when it is unable to provide a loadable object. For
example, the node_load() function for the 'node/%node/edit' menu item will
return FALSE for the path 'node/999/edit' if a node with a node ID of 999
does not exist. The menu routing system will return a 404 error in this case.

@subsection sub_argument_wildcards Argument Wildcards
You can also define a %wildcard_to_arg() function (for the example menu
entry above this would be 'mymodule_abc_to_arg()'). The _to_arg() function
is invoked to retrieve a value that is used in the path in place of the
wildcard. A good example is user.module, which defines
user_uid_optional_to_arg() (corresponding to the menu entry
'tracker/%user_uid_optional'). This function returns the user ID of the
current user.

The _to_arg() function will get called with three arguments:
- $arg: A string representing whatever argument may have been supplied by
  the caller (this is particularly useful if you want the _to_arg()
  function only supply a (default) value if no other value is specified,
  as in the case of user_uid_optional_to_arg().
- $map: An array of all path fragments (e.g. array('node','123','edit') for
  'node/123/edit').
- $index: An integer indicating which element of $map corresponds to $arg.

_load() and _to_arg() functions may seem similar at first glance, but they
have different purposes and are called at different times. _load()
functions are called when the menu system is collecting arguments to pass
to the callback functions defined for the menu item. _to_arg() functions
are called when the menu system is generating links to related paths, such
as the tabs for a set of MENU_LOCAL_TASK items.

@section sec_render_tabs Rendering Menu Items As Tabs
You can also make groups of menu items to be rendered (by default) as tabs
on a page. To do that, first create one menu item of type MENU_NORMAL_ITEM,
with your chosen path, such as 'foo'. Then duplicate that menu item, using a
subdirectory path, such as 'foo/tab1', and changing the type to
MENU_DEFAULT_LOCAL_TASK to make it the default tab for the group. Then add
the additional tab items, with paths such as "foo/tab2" etc., with type
MENU_LOCAL_TASK. Example:
@code
// Make "Foo settings" appear on the admin Config page
$items['admin/config/system/foo'] = array(
  'title' => 'Foo settings',
  'type' => MENU_NORMAL_ITEM,
  // Page callback, etc. need to be added here.
);
// Make "Tab 1" the main tab on the "Foo settings" page
$items['admin/config/system/foo/tab1'] = array(
  'title' => 'Tab 1',
  'type' => MENU_DEFAULT_LOCAL_TASK,
  // Access callback, page callback, and theme callback will be inherited
  // from 'admin/config/system/foo', if not specified here to override.
);
// Make an additional tab called "Tab 2" on "Foo settings"
$items['admin/config/system/foo/tab2'] = array(
  'title' => 'Tab 2',
  'type' => MENU_LOCAL_TASK,
  // Page callback and theme callback will be inherited from
  // 'admin/config/system/foo', if not specified here to override.
  // Need to add access callback or access arguments.
);
@endcode

@return
  An array of menu items. Each menu item has a key corresponding to the
  Drupal path being registered. The corresponding array value is an
  associative array that may contain the following key-value pairs:
  - "title": Required. The untranslated title of the menu item.
  - "title callback": Function to generate the title; defaults to t().
    If you require only the raw string to be output, set this to FALSE.
  - "title arguments": Arguments to send to t() or your custom callback,
    with path component substitution as described above.
  - "description": The untranslated description of the menu item.
  - "page callback": The function to call to display a web page when the user
    visits the path. If omitted, the parent menu item's callback will be used
    instead.
  - "page arguments": An array of arguments to pass to the page callback
    function, with path component substitution as described above.
  - "delivery callback": The function to call to package the result of the
    page callback function and send it to the browser. Defaults to
    drupal_deliver_html_page() unless a value is inherited from a parent menu
    item. Note that this function is called even if the access checks fail,
    so any custom delivery callback function should take that into account.
    See drupal_deliver_html_page() for an example.
  - "access callback": A function returning TRUE if the user has access
    rights to this menu item, and FALSE if not. It can also be a boolean
    constant instead of a function, and you can also use numeric values
    (will be cast to boolean). Defaults to user_access() unless a value is
    inherited from the parent menu item; only MENU_DEFAULT_LOCAL_TASK items
    can inherit access callbacks. To use the user_access() default callback,
    you must specify the permission to check as 'access arguments' (see
    below).
  - "access arguments": An array of arguments to pass to the access callback
    function, with path component substitution as described above. If the
    access callback is inherited (see above), the access arguments will be
    inherited with it, unless overridden in the child menu item.
  - "theme callback": (optional) A function returning the machine-readable
    name of the theme that will be used to render the page. If not provided,
    the value will be inherited from a parent menu item. If there is no
    theme callback, or if the function does not return the name of a current
    active theme on the site, the theme for this page will be determined by
    either hook_custom_theme() or the default theme instead. As a general
    rule, the use of theme callback functions should be limited to pages
    whose functionality is very closely tied to a particular theme, since
    they can only be overridden by modules which specifically target those
    pages in hook_menu_alter(). Modules implementing more generic theme
    switching functionality (for example, a module which allows the theme to
    be set dynamically based on the current user's role) should use
    hook_custom_theme() instead.
  - "theme arguments": An array of arguments to pass to the theme callback
    function, with path component substitution as described above.
  - "file": A file that will be included before the page callback is called;
    this allows page callback functions to be in separate files. The file
    should be relative to the implementing module's directory unless
    otherwise specified by the "file path" option. Does not apply to other
    callbacks (only page callback).
  - "file path": The path to the directory containing the file specified in
    "file". This defaults to the path to the module implementing the hook.
  - "load arguments": An array of arguments to be passed to each of the
    wildcard object loaders in the path, after the path argument itself.
    For example, if a module registers path node/%node/revisions/%/view
    with load arguments set to array(3), the '%node' in the path indicates
    that the loader function node_load() will be called with the second
    path component as the first argument. The 3 in the load arguments
    indicates that the fourth path component will also be passed to
    node_load() (numbering of path components starts at zero). So, if path
    node/12/revisions/29/view is requested, node_load(12, 29) will be called.
    There are also two "magic" values that can be used in load arguments.
    "%index" indicates the index of the wildcard path component. "%map"
    indicates the path components as an array. For example, if a module
    registers for several paths of the form 'user/%user_category/edit/*', all
    of them can use the same load function user_category_load(), by setting
    the load arguments to array('%map', '%index'). For instance, if the user
    is editing category 'foo' by requesting path 'user/32/edit/foo', the load
    function user_category_load() will be called with 32 as its first
    argument, the array ('user', 32, 'edit', 'foo') as the map argument,
    and 1 as the index argument (because %user_category is the second path
    component and numbering starts at zero). user_category_load() can then
    use these values to extract the information that 'foo' is the category
    being requested.
  - "weight": An integer that determines the relative position of items in
    the menu; higher-weighted items sink. Defaults to 0. Menu items with the
    same weight are ordered alphabetically.
  - "menu_name": Optional. Set this to a custom menu if you don't want your
    item to be placed in Navigation.
  - "expanded": Optional. If set to TRUE, and if a menu link is provided for
    this menu item (as a result of other properties), then the menu link is
    always expanded, equivalent to its 'always expanded' checkbox being set
    in the UI.
  - "context": (optional) Defines the context a tab may appear in. By
    default, all tabs are only displayed as local tasks when being rendered
    in a page context. All tabs that should be accessible as contextual links
    in page region containers outside of the parent menu item's primary page
    context should be registered using one of the following contexts:
    - MENU_CONTEXT_PAGE: (default) The tab is displayed as local task for the
      page context only.
    - MENU_CONTEXT_INLINE: The tab is displayed as contextual link outside of
      the primary page context only.
    Contexts can be combined. For example, to display a tab both on a page
    and inline, a menu router item may specify:
    @code
      'context' => MENU_CONTEXT_PAGE | MENU_CONTEXT_INLINE,
    @endcode
  - "tab_parent": For local task menu items, the path of the task's parent
    item; defaults to the same path without the last component (e.g., the
    default parent for 'admin/people/create' is 'admin/people').
  - "tab_root": For local task menu items, the path of the closest non-tab
    item; same default as "tab_parent".
  - "position": Position of the block ('left' or 'right') on the system
    administration page for this item.
  - "type": A bitmask of flags describing properties of the menu item.
    Many shortcut bitmasks are provided as constants in menu.inc:
    - MENU_NORMAL_ITEM: Normal menu items show up in the menu tree and can be
      moved/hidden by the administrator.
    - MENU_CALLBACK: Callbacks simply register a path so that the correct
      information is generated when the path is accessed.
    - MENU_SUGGESTED_ITEM: Modules may "suggest" menu items that the
      administrator may enable.
    - MENU_LOCAL_ACTION: Local actions are menu items that describe actions
      on the parent item such as adding a new user or block, and are
      rendered in the action-links list in your theme.
    - MENU_LOCAL_TASK: Local tasks are menu items that describe different
      displays of data, and are generally rendered as tabs.
    - MENU_DEFAULT_LOCAL_TASK: Every set of local tasks should provide one
      "default" task, which should display the same page as the parent item.
    If the "type" element is omitted, MENU_NORMAL_ITEM is assumed.
  - "options": An array of options to be passed to l() when generating a link
    from this menu item. Note that the "options" parameter has no effect on
    MENU_LOCAL_TASK, MENU_DEFAULT_LOCAL_TASK, and MENU_LOCAL_ACTION items.

For a detailed usage example, see page_example.module.
For comprehensive documentation on the menu system, see
http://drupal.org/node/102338.
```

## Code

```php
function hook_menu() {
  $items['example'] = array(
    'title' => 'Example Page',
    'page callback' => 'example_page',
    'access arguments' => array('access content'),
    'type' => MENU_SUGGESTED_ITEM,
  );
  $items['example/feed'] = array(
    'title' => 'Example RSS feed',
    'page callback' => 'example_feed',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
  );

  return $items;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_menu()".

- [update_test_menu()](../../update/tests/update_test.module/update_test_menu.md) — `modules/update/tests/update_test.module`
- [aggregator_menu()](../../aggregator/aggregator.module/aggregator_menu.md) — `modules/aggregator/aggregator.module`
- [aggregator_test_menu()](../../aggregator/tests/aggregator_test.module/aggregator_test_menu.md) — `modules/aggregator/tests/aggregator_test.module`
- [announce_feed_test_menu()](../../announcements_feed/tests/announce_feed_test.module/announce_feed_test_menu.md) — `modules/announcements_feed/tests/announce_feed_test.module`
- [announcements_feed_menu()](../../announcements_feed/announcements_feed.module/announcements_feed_menu.md) — `modules/announcements_feed/announcements_feed.module`
- [ajax_forms_test_menu()](../../simpletest/tests/ajax_forms_test.module/ajax_forms_test_menu.md) — `modules/simpletest/tests/ajax_forms_test.module`
- [ajax_test_menu()](../../simpletest/tests/ajax_test.module/ajax_test_menu.md) — `modules/simpletest/tests/ajax_test.module`
- [batch_test_menu()](../../simpletest/tests/batch_test.module/batch_test_menu.md) — `modules/simpletest/tests/batch_test.module`
- [common_test_menu()](../../simpletest/tests/common_test.module/common_test_menu.md) — `modules/simpletest/tests/common_test.module`
- [database_test_menu()](../../simpletest/tests/database_test.module/database_test_menu.md) — `modules/simpletest/tests/database_test.module`
- [entity_query_access_test_menu()](../../simpletest/tests/entity_query_access_test.module/entity_query_access_test_menu.md) — `modules/simpletest/tests/entity_query_access_test.module`
- [error_test_menu()](../../simpletest/tests/error_test.module/error_test_menu.md) — `modules/simpletest/tests/error_test.module`
- [file_test_menu()](../../simpletest/tests/file_test.module/file_test_menu.md) — `modules/simpletest/tests/file_test.module`
- [form_test_menu()](../../simpletest/tests/form_test.module/form_test_menu.md) — `modules/simpletest/tests/form_test.module`
- [menu_test_menu()](../../simpletest/tests/menu_test.module/menu_test_menu.md) — `modules/simpletest/tests/menu_test.module`
- [module_test_menu()](../../simpletest/tests/module_test.module/module_test_menu.md) — `modules/simpletest/tests/module_test.module`
- [session_test_menu()](../../simpletest/tests/session_test.module/session_test_menu.md) — `modules/simpletest/tests/session_test.module`
- [system_test_menu()](../../simpletest/tests/system_test.module/system_test_menu.md) — `modules/simpletest/tests/system_test.module`
- [theme_test_menu()](../../simpletest/tests/theme_test.module/theme_test_menu.md) — `modules/simpletest/tests/theme_test.module`
- [url_alter_test_menu()](../../simpletest/tests/url_alter_test.module/url_alter_test_menu.md) — `modules/simpletest/tests/url_alter_test.module`
- [block_menu()](../../block/block.module/block_menu.md) — `modules/block/block.module`
- [blog_menu()](../../blog/blog.module/blog_menu.md) — `modules/blog/blog.module`
- [book_menu()](../../book/book.module/book_menu.md) — `modules/book/book.module`
- [comment_menu()](../../comment/comment.module/comment_menu.md) — `modules/comment/comment.module`
- [contact_menu()](../../contact/contact.module/contact_menu.md) — `modules/contact/contact.module`
- [dashboard_menu()](../../dashboard/dashboard.module/dashboard_menu.md) — `modules/dashboard/dashboard.module`
- [dblog_menu()](../../dblog/dblog.module/dblog_menu.md) — `modules/dblog/dblog.module`
- [field_test_menu()](../../field/tests/field_test.module/field_test_menu.md) — `modules/field/tests/field_test.module`
- [field_ui_menu()](../../field_ui/field_ui.module/field_ui_menu.md) — `modules/field_ui/field_ui.module`
- [file_menu()](../../file/file.module/file_menu.md) — `modules/file/file.module`
- [file_module_test_menu()](../../file/tests/file_module_test.module/file_module_test_menu.md) — `modules/file/tests/file_module_test.module`
- [filter_menu()](../../filter/filter.module/filter_menu.md) — `modules/filter/filter.module`
- [forum_menu()](../../forum/forum.module/forum_menu.md) — `modules/forum/forum.module`
- [help_menu()](../../help/help.module/help_menu.md) — `modules/help/help.module`
- [image_menu()](../../image/image.module/image_menu.md) — `modules/image/image.module`
- [locale_menu()](../../locale/locale.module/locale_menu.md) — `modules/locale/locale.module`
- [locale_test_menu()](../../locale/tests/locale_test.module/locale_test_menu.md) — `modules/locale/tests/locale_test.module`
- [menu_menu()](../../menu/menu.module/menu_menu.md) — `modules/menu/menu.module`
- [node_menu()](../../node/node.module/node_menu.md) — `modules/node/node.module`
- [node_access_test_menu()](../../node/tests/node_access_test.module/node_access_test_menu.md) — `modules/node/tests/node_access_test.module`
- [openid_menu()](../../openid/openid.module/openid_menu.md) — `modules/openid/openid.module`
- [openid_test_menu()](../../openid/tests/openid_test.module/openid_test_menu.md) — `modules/openid/tests/openid_test.module`
- [overlay_menu()](../../overlay/overlay.module/overlay_menu.md) — `modules/overlay/overlay.module`
- [path_menu()](../../path/path.module/path_menu.md) — `modules/path/path.module`
- [poll_menu()](../../poll/poll.module/poll_menu.md) — `modules/poll/poll.module`
- [profile_menu()](../../profile/profile.module/profile_menu.md) — `modules/profile/profile.module`
- [search_menu()](../../search/search.module/search_menu.md) — `modules/search/search.module`
- [search_embedded_form_menu()](../../search/tests/search_embedded_form.module/search_embedded_form_menu.md) — `modules/search/tests/search_embedded_form.module`
- [shortcut_menu()](../../shortcut/shortcut.module/shortcut_menu.md) — `modules/shortcut/shortcut.module`
- [simpletest_menu()](../../simpletest/simpletest.module/simpletest_menu.md) — `modules/simpletest/simpletest.module`
- [statistics_menu()](../../statistics/statistics.module/statistics_menu.md) — `modules/statistics/statistics.module`
- [system_menu()](../system.module/system_menu.md) — `modules/system/system.module`
- [taxonomy_menu()](../../taxonomy/taxonomy.module/taxonomy_menu.md) — `modules/taxonomy/taxonomy.module`
- [toolbar_menu()](../../toolbar/toolbar.module/toolbar_menu.md) — `modules/toolbar/toolbar.module`
- [tracker_menu()](../../tracker/tracker.module/tracker_menu.md) — `modules/tracker/tracker.module`
- [translation_menu()](../../translation/translation.module/translation_menu.md) — `modules/translation/translation.module`
- [trigger_menu()](../../trigger/trigger.module/trigger_menu.md) — `modules/trigger/trigger.module`
- [update_menu()](../../update/update.module/update_menu.md) — `modules/update/update.module`
- [user_menu()](../../user/user.module/user_menu.md) — `modules/user/user.module`
- [user_form_test_menu()](../../user/tests/user_form_test.module/user_form_test_menu.md) — `modules/user/tests/user_form_test.module`
- [user_session_test_menu()](../../user/tests/user_session_test.module/user_session_test_menu.md) — `modules/user/tests/user_session_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
