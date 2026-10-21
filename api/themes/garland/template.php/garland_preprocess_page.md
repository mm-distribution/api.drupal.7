# garland_preprocess_page()

- **Type:** Function
- **File:** [`themes/garland/template.php`](_file.md), lines 56–115 · [local source](../../../../source/themes/garland/template.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php#L56-L115)
- **Module/theme:** garland

## Signature

```php
function garland_preprocess_page(&$variables)
```

## Documentation

```text
Override or insert variables into the page template.
```

## Code

```php
function garland_preprocess_page(&$variables) {
  // Move secondary tabs into a separate variable.
  $variables['tabs2'] = array(
    '#theme' => 'menu_local_tasks',
    '#secondary' => $variables['tabs']['#secondary'],
  );
  unset($variables['tabs']['#secondary']);

  if (isset($variables['main_menu'])) {
    $variables['primary_nav'] = theme('links__system_main_menu', array(
      'links' => $variables['main_menu'],
      'attributes' => array(
        'class' => array('links', 'inline', 'main-menu'),
      ),
      'heading' => array(
        'text' => t('Main menu'),
        'level' => 'h2',
        'class' => array('element-invisible'),
      )
    ));
  }
  else {
    $variables['primary_nav'] = FALSE;
  }
  if (isset($variables['secondary_menu'])) {
    $variables['secondary_nav'] = theme('links__system_secondary_menu', array(
      'links' => $variables['secondary_menu'],
      'attributes' => array(
        'class' => array('links', 'inline', 'secondary-menu'),
      ),
      'heading' => array(
        'text' => t('Secondary menu'),
        'level' => 'h2',
        'class' => array('element-invisible'),
      )
    ));
  }
  else {
    $variables['secondary_nav'] = FALSE;
  }

  // Prepare header.
  $site_fields = array();
  if (!empty($variables['site_name'])) {
    $site_fields[] = $variables['site_name'];
  }
  if (!empty($variables['site_slogan'])) {
    $site_fields[] = $variables['site_slogan'];
  }
  $variables['site_title'] = implode(' ', $site_fields);
  if (!empty($site_fields)) {
    $site_fields[0] = '<span>' . $site_fields[0] . '</span>';
  }
  $variables['site_html'] = implode(' ', $site_fields);

  // Set a variable for the site name title and logo alt attributes text.
  $slogan_text = $variables['site_slogan'];
  $site_name_text = $variables['site_name'];
  $variables['site_name_and_slogan'] = $site_name_text . ' ' . $slogan_text;
}
```

---
_Drupal 7.103 · [themes/garland/template.php](https://github.com/drupal/drupal/blob/7.103/themes/garland/template.php) · Licensed GPL-2.0-or-later (see LICENSE)._
