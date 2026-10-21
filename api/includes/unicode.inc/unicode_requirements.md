# unicode_requirements()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 139–166 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L139-L166)

## Signature

```php
function unicode_requirements()
```

## Documentation

```text
Returns Unicode library status and errors.
```

## Code

```php
function unicode_requirements() {
  // Ensure translations don't break during installation.
  $t = get_t();

  $libraries = array(
    UNICODE_SINGLEBYTE => $t('Standard PHP'),
    UNICODE_MULTIBYTE => $t('PHP Mbstring Extension'),
    UNICODE_ERROR => $t('Error'),
  );
  $severities = array(
    UNICODE_SINGLEBYTE => REQUIREMENT_WARNING,
    UNICODE_MULTIBYTE => REQUIREMENT_OK,
    UNICODE_ERROR => REQUIREMENT_ERROR,
  );
  list($library, $description) = _unicode_check();

  $requirements['unicode'] = array(
    'title' => $t('Unicode library'),
    'value' => $libraries[$library],
  );
  if ($description) {
    $requirements['unicode']['description'] = $description;
  }

  $requirements['unicode']['severity'] = $severities[$library];

  return $requirements;
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
