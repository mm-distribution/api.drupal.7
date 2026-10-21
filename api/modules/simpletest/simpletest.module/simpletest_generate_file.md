# simpletest_generate_file()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 517–541 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L517-L541)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_generate_file($filename, $width, $lines, $type = 'binary-text')
```

## Documentation

```text
Generate test file.
```

## Code

```php
function simpletest_generate_file($filename, $width, $lines, $type = 'binary-text') {
  $text = '';
  for ($i = 0; $i < $lines; $i++) {
    // Generate $width - 1 characters to leave space for the "\n" character.
    for ($j = 0; $j < $width - 1; $j++) {
      switch ($type) {
        case 'text':
          $text .= chr(rand(32, 126));
          break;
        case 'binary':
          $text .= chr(rand(0, 31));
          break;
        case 'binary-text':
        default:
          $text .= rand(0, 1);
          break;
      }
    }
    $text .= "\n";
  }

  // Create filename.
  file_put_contents('public://' . $filename . '.txt', $text);
  return $filename;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
