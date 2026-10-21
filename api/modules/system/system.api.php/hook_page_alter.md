# hook_page_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1627–1633 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1627-L1633)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_page_alter(&$page)
```

## Documentation

```text
Perform alterations before a page is rendered.

Use this hook when you want to remove or alter elements at the page
level, or add elements at the page level that depend on an other module's
elements (this hook runs after hook_page_build().

If you are making changes to entities such as forms, menus, or user
profiles, use those objects' native alter hooks instead (hook_form_alter(),
for example).

The $page array contains top level elements for each block region:
@code
  $page['page_top']
  $page['header']
  $page['sidebar_first']
  $page['content']
  $page['sidebar_second']
  $page['page_bottom']
@endcode

The 'content' element contains the main content of the current page, and its
structure will vary depending on what module is responsible for building the
page. Some legacy modules may not return structured content at all: their
pre-rendered markup will be located in $page['content']['main']['#markup'].

Pages built by Drupal's core Node and Blog modules use a standard structure:

@code
  // Node body.
  $page['content']['system_main']['nodes'][$nid]['body']
  // Array of links attached to the node (add comments, read more).
  $page['content']['system_main']['nodes'][$nid]['links']
  // The node object itself.
  $page['content']['system_main']['nodes'][$nid]['#node']
  // The results pager.
  $page['content']['system_main']['pager']
@endcode

Blocks may be referenced by their module/delta pair within a region:
@code
  // The login block in the first sidebar region.
  $page['sidebar_first']['user_login']['#block'];
@endcode

@param $page
  Nested array of renderable elements that make up the page.

@see hook_page_build()
@see drupal_render_page()
```

## Code

```php
function hook_page_alter(&$page) {
  // Add help text to the user login block.
  $page['sidebar_first']['user_login']['help'] = array(
    '#weight' => -10,
    '#markup' => t('To post comments or add new content, you first have to log in.'),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_page_alter()".

- [announcements_feed_page_alter()](../../announcements_feed/announcements_feed.module/announcements_feed_page_alter.md) — `modules/announcements_feed/announcements_feed.module`
- [book_page_alter()](../../book/book.module/book_page_alter.md) — `modules/book/book.module`
- [overlay_page_alter()](../../overlay/overlay.module/overlay_page_alter.md) — `modules/overlay/overlay.module`
- [shortcut_page_alter()](../../shortcut/shortcut.module/shortcut_page_alter.md) — `modules/shortcut/shortcut.module`
- [system_page_alter()](../system.module/system_page_alter.md) — `modules/system/system.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
