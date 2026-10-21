# CommentHelperCase::setCommentPreview()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 152–167 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L152-L167)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
- **Module/theme:** comment

## Signature

```php
function setCommentPreview($mode)
```

## Documentation

```text
Set comment preview setting.

@param int $mode
  Preview value.
```

## Code

```php
  function setCommentPreview($mode) {
    switch ($mode) {
      case DRUPAL_DISABLED:
        $mode_text = 'disabled';
        break;

      case DRUPAL_OPTIONAL:
        $mode_text = 'optional';
        break;

      case DRUPAL_REQUIRED:
        $mode_text = 'required';
        break;
    }
    $this->setCommentSettings('comment_preview', $mode, format_string('Comment preview @mode_text.', array('@mode_text' => $mode_text)));
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
