# HelpTestCase::verifyHelp()

- **Type:** Method
- **File:** [`modules/help/help.test`](../_file.md), lines 80–90 · [local source](../../../../../source/modules/help/help.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test#L80-L90)
- **Class:** [HelpTestCase](../HelpTestCase.md)
- **Module/theme:** help

## Signature

```php
protected function verifyHelp($response = 200)
```

## Documentation

```text
Verifies the logged in user has access to the various help nodes.

@param integer $response
  An HTTP response code.
```

## Code

```php
  protected function verifyHelp($response = 200) {
    foreach ($this->modules as $module => $name) {
      // View module help node.
      $this->drupalGet('admin/help/' . $module);
      $this->assertResponse($response);
      if ($response == 200) {
        $this->assertTitle($name . ' | Drupal', format_string('%module title was displayed', array('%module' => $module)));
        $this->assertRaw('<h1 class="page-title">' . t($name) . '</h1>', format_string('%module heading was displayed', array('%module' => $module)));
       }
    }
  }
```

---
_Drupal 7.103 · [modules/help/help.test](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test) · Licensed GPL-2.0-or-later (see LICENSE)._
