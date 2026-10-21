# CommentHelperCase::commentContactInfoAvailable()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 220–222 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L220-L222)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
- **Module/theme:** comment

## Signature

```php
function commentContactInfoAvailable()
```

## Documentation

```text
Check for contact info.

@return boolean Contact info is available.
```

## Code

```php
  function commentContactInfoAvailable() {
    return preg_match('/(input).*?(name="name").*?(input).*?(name="mail").*?(input).*?(name="homepage")/s', $this->drupalGetContent());
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
