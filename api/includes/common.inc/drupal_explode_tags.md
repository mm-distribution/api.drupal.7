# drupal_explode_tags()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7804–7823 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7804-L7823)

## Signature

```php
function drupal_explode_tags($tags)
```

## Documentation

```text
Explodes a string of tags into an array.

@see drupal_implode_tags()
```

## Code

```php
function drupal_explode_tags($tags) {
  // This regexp allows the following types of user input:
  // this, "somecompany, llc", "and ""this"" w,o.rks", foo bar
  $regexp = '%(?:^|,\ *)("(?>[^"]*)(?>""[^"]* )*"|(?: [^",]*))%x';
  preg_match_all($regexp, $tags, $matches);
  $typed_tags = array_unique($matches[1]);

  $tags = array();
  foreach ($typed_tags as $tag) {
    // If a user has escaped a term (to demonstrate that it is a group,
    // or includes a comma or quote character), we remove the escape
    // formatting so to save the term into the database as the user intends.
    $tag = trim(str_replace('""', '"', preg_replace('/^"(.*)"$/', '\1', $tag)));
    if ($tag != "") {
      $tags[] = $tag;
    }
  }

  return $tags;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
