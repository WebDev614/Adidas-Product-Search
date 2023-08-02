# custom_css.py

css_string = """
<style>
    .image-grid {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
    }

    .image-row {
      display: flex;
      justify-content: center;
      margin: 10px 0;
    }

    .image-item {
      margin: 5px;
    }

    .flip-card {
      background-color: transparent;
      width: 100%;
      height: 100%;
      perspective: 1000px;
    }

    .flip-card-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.6s;
      transform-style: preserve-3d;
    }

    .flip-card:hover .flip-card-inner {
      transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
    }

    .flip-card-front {
      background-color: #f1f1f1;
    }

    .flip-card-back {
      background-color: #4CAF50;
      color: white;
      transform: rotateY(180deg);
    }
</style>
"""
