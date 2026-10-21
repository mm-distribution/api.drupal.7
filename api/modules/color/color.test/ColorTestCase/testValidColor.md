# ColorTestCase::testValidColor()

- **Type:** Method
- **File:** [`modules/color/color.test`](../_file.md), lines 114–132 · [local source](../../../../../source/modules/color/color.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test#L114-L132)
- **Class:** [ColorTestCase](../ColorTestCase.md)
- **Module/theme:** color

## Signature

```php
function testValidColor()
```

## Documentation

```text
Tests whether the provided color is valid.
```

## Code

```php
  function testValidColor() {
    variable_set('theme_default', 'bartik');
    $settings_path = 'admin/appearance/settings/bartik';

    $this->drupalLogin($this->big_user);
    $edit['scheme'] = '';

    foreach ($this->colorTests as $color => $is_valid) {
      $edit['palette[bg]'] = $color;
      $this->drupalPost($settings_path, $edit, t('Save configuration'));

      if ($is_valid) {
        $this->assertText('The configuration options have been saved.');
      }
      else {
        $this->assertText('Main background must be a valid hexadecimal CSS color value.');
      }
    }
  }
```

---
_Drupal 7.103 · [modules/color/color.test](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test) · Licensed GPL-2.0-or-later (see LICENSE)._
