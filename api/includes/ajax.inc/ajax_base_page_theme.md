# ajax_base_page_theme()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 435–449 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L435-L449)
- **Topics:** [ajax](../../topics/ajax.md)

## Signature

```php
function ajax_base_page_theme()
```

## Documentation

```text
Theme callback for Ajax requests.

Many different pages can invoke an Ajax request to system/ajax or another
generic Ajax path. It is almost always desired for an Ajax response to be
rendered using the same theme as the base page, because most themes are built
with the assumption that they control the entire page, so if the CSS for two
themes are both loaded for a given page, they may conflict with each other.
For example, Bartik is Drupal's default theme, and Seven is Drupal's default
administration theme. Depending on whether the "Use the administration theme
when editing or creating content" checkbox is checked, the node edit form may
be displayed in either theme, but the Ajax response to the Field module's
"Add another item" button should be rendered using the same theme as the rest
of the page. Therefore, system_menu() sets the 'theme callback' for
'system/ajax' to this function, and it is recommended that modules
implementing other generic Ajax paths do the same.

@see system_menu()
@see file_menu()
```

## Code

```php
function ajax_base_page_theme() {
  if (!empty($_POST['ajax_page_state']['theme']) && !empty($_POST['ajax_page_state']['theme_token'])) {
    $theme = $_POST['ajax_page_state']['theme'];
    $token = $_POST['ajax_page_state']['theme_token'];

    // Prevent a request forgery from giving a person access to a theme they
    // shouldn't be otherwise allowed to see. However, since everyone is allowed
    // to see the default theme, token validation isn't required for that, and
    // bypassing it allows most use-cases to work even when accessed from the
    // page cache.
    if ($theme === variable_get('theme_default', 'bartik') || drupal_valid_token($token, $theme)) {
      return $theme;
    }
  }
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
