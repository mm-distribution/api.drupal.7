# ColorUnitTestCase::setUp()

- **Type:** Method
- **File:** [`modules/color/color.test`](../_file.md), lines 156–170 · [local source](../../../../../source/modules/color/color.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test#L156-L170)
- **Class:** [ColorUnitTestCase](../ColorUnitTestCase.md)
- **Module/theme:** color

## Signature

```php
public function setUp()
```

## Documentation

```text
Set up the test environment.
```

## Code

```php
  public function setUp() {
    drupal_load('module', 'color');
    parent::setUp();

    $this->test_values = array(
      array(array(0.2, 0.4, 0.8), TRUE, '#3366cc'),
      array(array(51, 102, 204), FALSE, '#3366cc'),
      array(array(6, 120, 190), FALSE, '#0678be'),
      array(array(192, 192, 192), FALSE, '#c0c0c0'),
      array(array(255, 255, 0), FALSE, '#ffff00'),
      array(array(128, 0, 128), FALSE, '#800080'),
      array(array(0.6, 0.8, 1), TRUE, '#99ccff'),
      array(array(221, 72, 20), FALSE, '#dd4814'),
    );
  }
```

---
_Drupal 7.103 · [modules/color/color.test](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test) · Licensed GPL-2.0-or-later (see LICENSE)._
