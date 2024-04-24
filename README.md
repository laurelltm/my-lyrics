# My Lyrics - Book File Support

Welcome to the support page for **My Lyrics**. This guide provides instructions on creating and using book files with the My Lyrics app. If you have any questions, issues, or need assistance, please contact us:

- **Email**: [laurelltm@gmail.com](mailto:laurelltm@gmail.com)

We aim to respond to all inquiries within 24-48 hours. Thank you for using My Lyrics!

## What is a Library File?
A library file is a compressed file with the extension `.zip` or `.books`. It contains multiple book files, each stored as gzipped JSON files. For example, a library file might include:

- `book1.gz`
- `book2.gz`
- `book3.gz`

Each book file represents a collection of songs in JSON format, gzipped for compression.

## What is a Single Book File?
A single book file can be compressed with the same extensions (`.zip` or `.books`). Additionally, non-compressed JSON files are also supported.

## JSON File Structure
A book in JSON format has a specific structure. Here's an example layout:

```json
{
  "title": "Title of the book",
  "coverImage": "base 64 encoded image data",
  "songs": [
    {
      "title": "Title of first song",
      "number": 1,
      "verses": [
        {
          "number": 1,
          "sentences": [
            "First sentence of the first verse",
            "Second sentence of the first verse"
          ]
        }
      ]
    }
  ]
}
```

- **Title**: The title of the book.
- **Cover Image**: A base64-encoded image representing the book's cover. Optional, but highly recommended.
- **Songs**: A list of songs within the book.
  - **Title**: The title of each song.
  - **Number**: The song's number. Optional.
  - **Verses**: The verses contained in each song.
    - **Number**: The verse's number within the song. Optional.
    - **Sentences**: An array of sentences forming the verse.

### Example JSON File
To better understand the format, refer to [`lorem_ipsum_songbook.json`](./lorem_ipsum_songbook.json) provided with this README.

## How to Create Book Files
To create a book file for My Lyrics, follow these steps:

1. Create a JSON file with the structure described above.
2. Compress the JSON file using a tool like `gzip`.
3. Rename the compressed file to have a `.books` extension.
4. Transfer the `.books` file to your iPhone.
5. Open the file with the My Lyrics app.

We hope this guide helps you create and manage book files for My Lyrics. If you need additional assistance, don't hesitate to contact us at the email address provided above.
