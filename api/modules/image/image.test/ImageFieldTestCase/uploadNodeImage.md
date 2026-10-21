# ImageFieldTestCase::uploadNodeImage()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 113–124 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L113-L124)
- **Class:** [ImageFieldTestCase](../ImageFieldTestCase.md)
- **Module/theme:** image

## Signature

```php
function uploadNodeImage($image, $field_name, $type)
```

## Documentation

```text
Upload an image to a node.

@param $image
  A file object representing the image to upload.
@param $field_name
  Name of the image field the image should be attached to.
@param $type
  The type of node to create.
```

## Code

```php
  function uploadNodeImage($image, $field_name, $type) {
    $edit = array(
      'title' => $this->randomName(),
    );
    $edit['files[' . $field_name . '_' . LANGUAGE_NONE . '_0]'] = drupal_realpath($image->uri);
    $this->drupalPost('node/add/' . $type, $edit, t('Save'));

    // Retrieve ID of the newly created node from the current URL.
    $matches = array();
    preg_match('/node\/([0-9]+)/', $this->getUrl(), $matches);
    return isset($matches[1]) ? $matches[1] : FALSE;
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
