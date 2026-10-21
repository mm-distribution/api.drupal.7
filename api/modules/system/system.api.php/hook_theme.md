# hook_theme()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2304–2327 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2304-L2327)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_theme($existing, $type, $theme, $path)
```

## Documentation

```text
Register a module (or theme's) theme implementations.

The implementations declared by this hook have two purposes: either they
specify how a particular render array is to be rendered as HTML (this is
usually the case if the theme function is assigned to the render array's
#theme property), or they return the HTML that should be returned by an
invocation of theme(). See
@link http://drupal.org/node/933976 Using the theme layer Drupal 7.x @endlink
for more information on how to implement theme hooks.

The following parameters are all optional.

@param array $existing
  An array of existing implementations that may be used for override
  purposes. This is primarily useful for themes that may wish to examine
  existing implementations to extract data (such as arguments) so that
  it may properly register its own, higher priority implementations.
@param $type
  Whether a theme, module, etc. is being processed. This is primarily useful
  so that themes tell if they are the actual theme being called or a parent
  theme. May be one of:
  - 'module': A module is being checked for theme implementations.
  - 'base_theme_engine': A theme engine is being checked for a theme that is
    a parent of the actual theme being used.
  - 'theme_engine': A theme engine is being checked for the actual theme
    being used.
  - 'base_theme': A base theme is being checked for theme implementations.
  - 'theme': The actual theme in use is being checked.
@param $theme
  The actual name of theme, module, etc. that is being being processed.
@param $path
  The directory path of the theme or module, so that it doesn't need to be
  looked up.

@return array
  An associative array of theme hook information. The keys on the outer
  array are the internal names of the hooks, and the values are arrays
  containing information about the hook. Each information array must contain
  either a 'variables' element or a 'render element' element, but not both.
  Use 'render element' if you are theming a single element or element tree
  composed of elements, such as a form array, a page array, or a single
  checkbox element. Use 'variables' if your theme implementation is
  intended to be called directly through theme() and has multiple arguments
  for the data and style; in this case, the variables not supplied by the
  calling function will be given default values and passed to the template
  or theme function. The returned theme information array can contain the
  following key/value pairs:
  - variables: (see above) Each array key is the name of the variable, and
    the value given is used as the default value if the function calling
    theme() does not supply it. Template implementations receive each array
    key as a variable in the template file (so they must be legal PHP
    variable names). Function implementations are passed the variables in a
    single $variables function argument.
  - render element: (see above) The name of the renderable element or element
    tree to pass to the theme function. This name is used as the name of the
    variable that holds the renderable element or tree in preprocess and
    process functions.
  - file: The file the implementation resides in. This file will be included
    prior to the theme being rendered, to make sure that the function or
    preprocess function (as needed) is actually loaded; this makes it
    possible to split theme functions out into separate files quite easily.
  - path: Override the path of the file to be used. Ordinarily the module or
    theme path will be used, but if the file will not be in the default
    path, include it here. This path should be relative to the Drupal root
    directory.
  - template: If specified, this theme implementation is a template, and
    this is the template file without an extension. Do not put .tpl.php on
    this file; that extension will be added automatically by the default
    rendering engine (which is PHPTemplate). If 'path', above, is specified,
    the template should also be in this path.
  - function: If specified, this will be the function name to invoke for
    this implementation. If neither 'template' nor 'function' is specified,
    a default function name will be assumed. For example, if a module
    registers the 'node' theme hook, 'theme_node' will be assigned to its
    function. If the chameleon theme registers the node hook, it will be
    assigned 'chameleon_node' as its function.
  - base hook: A string declaring the base theme hook if this theme
    implementation is actually implementing a suggestion for another theme
    hook.
  - pattern: A regular expression pattern to be used to allow this theme
    implementation to have a dynamic name. The convention is to use __ to
    differentiate the dynamic portion of the theme. For example, to allow
    forums to be themed individually, the pattern might be: 'forum__'. Then,
    when the forum is themed, call:
    @code
    theme(array('forum__' . $tid, 'forum'), $forum)
    @endcode
  - preprocess functions: A list of functions used to preprocess this data.
    Ordinarily this won't be used; it's automatically filled in. By default,
    for a module this will be filled in as template_preprocess_HOOK. For
    a theme this will be filled in as phptemplate_preprocess and
    phptemplate_preprocess_HOOK as well as themename_preprocess and
    themename_preprocess_HOOK.
  - override preprocess functions: Set to TRUE when a theme does NOT want
    the standard preprocess functions to run. This can be used to give a
    theme FULL control over how variables are set. For example, if a theme
    wants total control over how certain variables in the page.tpl.php are
    set, this can be set to true. Please keep in mind that when this is used
    by a theme, that theme becomes responsible for making sure necessary
    variables are set.
  - type: (automatically derived) Where the theme hook is defined:
    'module', 'theme_engine', or 'theme'.
  - theme path: (automatically derived) The directory path of the theme or
    module, so that it doesn't need to be looked up.

@see hook_theme_registry_alter()
```

## Code

```php
function hook_theme($existing, $type, $theme, $path) {
  return array(
    'forum_display' => array(
      'variables' => array('forums' => NULL, 'topics' => NULL, 'parents' => NULL, 'tid' => NULL, 'sortby' => NULL, 'forum_per_page' => NULL),
    ),
    'forum_list' => array(
      'variables' => array('forums' => NULL, 'parents' => NULL, 'tid' => NULL),
    ),
    'forum_topic_list' => array(
      'variables' => array('tid' => NULL, 'topics' => NULL, 'sortby' => NULL, 'forum_per_page' => NULL),
    ),
    'forum_icon' => array(
      'variables' => array('new_posts' => NULL, 'num_posts' => 0, 'comment_mode' => 0, 'sticky' => 0),
    ),
    'status_report' => array(
      'render element' => 'requirements',
      'file' => 'system.admin.inc',
    ),
    'system_date_time_settings' => array(
      'render element' => 'form',
      'file' => 'system.admin.inc',
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_theme()".

- [phptemplate_theme()](../../../themes/engines/phptemplate/phptemplate.engine/phptemplate_theme.md) — `themes/engines/phptemplate/phptemplate.engine`
- [aggregator_theme()](../../aggregator/aggregator.module/aggregator_theme.md) — `modules/aggregator/aggregator.module`
- [announcements_feed_theme()](../../announcements_feed/announcements_feed.module/announcements_feed_theme.md) — `modules/announcements_feed/announcements_feed.module`
- [common_test_theme()](../../simpletest/tests/common_test.module/common_test_theme.md) — `modules/simpletest/tests/common_test.module`
- [nyan_cat_theme()](../../simpletest/tests/themes/engines/nyan_cat/nyan_cat.engine/nyan_cat_theme.md) — `modules/simpletest/tests/themes/engines/nyan_cat/nyan_cat.engine`
- [theme_test_theme()](../../simpletest/tests/theme_test.module/theme_test_theme.md) — `modules/simpletest/tests/theme_test.module`
- [block_theme()](../../block/block.module/block_theme.md) — `modules/block/block.module`
- [book_theme()](../../book/book.module/book_theme.md) — `modules/book/book.module`
- [color_theme()](../../color/color.module/color_theme.md) — `modules/color/color.module`
- [comment_theme()](../../comment/comment.module/comment_theme.md) — `modules/comment/comment.module`
- [dashboard_theme()](../../dashboard/dashboard.module/dashboard_theme.md) — `modules/dashboard/dashboard.module`
- [dblog_theme()](../../dblog/dblog.module/dblog_theme.md) — `modules/dblog/dblog.module`
- [field_theme()](../../field/field.module/field_theme.md) — `modules/field/field.module`
- [field_ui_theme()](../../field_ui/field_ui.module/field_ui_theme.md) — `modules/field_ui/field_ui.module`
- [file_theme()](../../file/file.module/file_theme.md) — `modules/file/file.module`
- [filter_theme()](../../filter/filter.module/filter_theme.md) — `modules/filter/filter.module`
- [forum_theme()](../../forum/forum.module/forum_theme.md) — `modules/forum/forum.module`
- [image_theme()](../../image/image.module/image_theme.md) — `modules/image/image.module`
- [locale_theme()](../../locale/locale.module/locale_theme.md) — `modules/locale/locale.module`
- [menu_theme()](../../menu/menu.module/menu_theme.md) — `modules/menu/menu.module`
- [node_theme()](../../node/node.module/node_theme.md) — `modules/node/node.module`
- [options_theme()](../../field/modules/options/options.module/options_theme.md) — `modules/field/modules/options/options.module`
- [overlay_theme()](../../overlay/overlay.module/overlay_theme.md) — `modules/overlay/overlay.module`
- [poll_theme()](../../poll/poll.module/poll_theme.md) — `modules/poll/poll.module`
- [profile_theme()](../../profile/profile.module/profile_theme.md) — `modules/profile/profile.module`
- [rdf_theme()](../../rdf/rdf.module/rdf_theme.md) — `modules/rdf/rdf.module`
- [search_theme()](../../search/search.module/search_theme.md) — `modules/search/search.module`
- [shortcut_theme()](../../shortcut/shortcut.module/shortcut_theme.md) — `modules/shortcut/shortcut.module`
- [simpletest_theme()](../../simpletest/simpletest.module/simpletest_theme.md) — `modules/simpletest/simpletest.module`
- [system_theme()](../system.module/system_theme.md) — `modules/system/system.module`
- [taxonomy_theme()](../../taxonomy/taxonomy.module/taxonomy_theme.md) — `modules/taxonomy/taxonomy.module`
- [toolbar_theme()](../../toolbar/toolbar.module/toolbar_theme.md) — `modules/toolbar/toolbar.module`
- [trigger_theme()](../../trigger/trigger.module/trigger_theme.md) — `modules/trigger/trigger.module`
- [update_theme()](../../update/update.module/update_theme.md) — `modules/update/update.module`
- [user_theme()](../../user/user.module/user_theme.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
