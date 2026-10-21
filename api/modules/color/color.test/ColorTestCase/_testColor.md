# ColorTestCase::_testColor()

- **Type:** Method
- **File:** [`modules/color/color.test`](../_file.md), lines 71–109 · [local source](../../../../../source/modules/color/color.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test#L71-L109)
- **Class:** [ColorTestCase](../ColorTestCase.md)
- **Module/theme:** color

## Signature

```php
function _testColor($theme, $test_values)
```

## Documentation

```text
Tests the Color module functionality using the given theme.
```

## Code

```php
  function _testColor($theme, $test_values) {
    variable_set('theme_default', $theme);
    $settings_path = 'admin/appearance/settings/' . $theme;

    $this->drupalLogin($this->big_user);
    $this->drupalGet($settings_path);
    $this->assertResponse(200);
    $edit['scheme'] = '';
    $edit[$test_values['palette_input']] = '#123456';
    $this->drupalPost($settings_path, $edit, t('Save configuration'));

    $this->drupalGet('<front>');
    $stylesheets = variable_get('color_' . $theme . '_stylesheets', array());
    $this->assertPattern('|' . file_create_url($stylesheets[0]) . '|', 'Make sure the color stylesheet is included in the content. (' . $theme . ')');

    $stylesheet_content = join("\n", file($stylesheets[0]));
    $this->assertTrue(strpos($stylesheet_content, 'color: #123456') !== FALSE, 'Make sure the color we changed is in the color stylesheet. (' . $theme . ')');

    $this->drupalGet($settings_path);
    $this->assertResponse(200);
    $edit['scheme'] = $test_values['scheme'];
    $this->drupalPost($settings_path, $edit, t('Save configuration'));

    $this->drupalGet('<front>');
    $stylesheets = variable_get('color_' . $theme . '_stylesheets', array());
    $stylesheet_content = join("\n", file($stylesheets[0]));
    $this->assertTrue(strpos($stylesheet_content, 'color: ' . $test_values['scheme_color']) !== FALSE, 'Make sure the color we changed is in the color stylesheet. (' . $theme . ')');

    // Test with aggregated CSS turned on.
    variable_set('preprocess_css', 1);
    $this->drupalGet('<front>');
    $stylesheets = variable_get('drupal_css_cache_files', array());
    $stylesheet_content = '';
    foreach ($stylesheets as $key => $uri) {
      $stylesheet_content .= join("\n", file(drupal_realpath($uri)));
    }
    $this->assertTrue(strpos($stylesheet_content, 'public://') === FALSE, 'Make sure the color paths have been translated to local paths. (' . $theme . ')');
    variable_set('preprocess_css', 0);
  }
```

---
_Drupal 7.103 · [modules/color/color.test](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test) · Licensed GPL-2.0-or-later (see LICENSE)._
