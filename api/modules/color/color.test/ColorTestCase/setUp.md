# ColorTestCase::setUp()

- **Type:** Method
- **File:** [`modules/color/color.test`](../_file.md), lines 24–57 · [local source](../../../../../source/modules/color/color.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test#L24-L57)
- **Class:** [ColorTestCase](../ColorTestCase.md)
- **Module/theme:** color

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('color');

    // Create users.
    $this->big_user = $this->drupalCreateUser(array('administer themes'));

    // This tests the color module in both Bartik and Garland.
    $this->themes = array(
      'bartik' => array(
        'palette_input' => 'palette[bg]',
        'scheme' => 'slate',
        'scheme_color' => '#3b3b3b',
      ),
      'garland' => array(
        'palette_input' => 'palette[link]',
        'scheme' => 'greenbeam',
        'scheme_color' => '#0c7a00',
      ),
    );
    theme_enable(array_keys($this->themes));

    // Array filled with valid and not valid color values
    $this->colorTests = array(
      '#000' => TRUE,
      '#123456' => TRUE,
      '#abcdef' => TRUE,
      '#0' => FALSE,
      '#00' => FALSE,
      '#0000' => FALSE,
      '#00000' => FALSE,
      '123456' => FALSE,
      '#00000g' => FALSE,
    );
  }
```

---
_Drupal 7.103 · [modules/color/color.test](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test) · Licensed GPL-2.0-or-later (see LICENSE)._
