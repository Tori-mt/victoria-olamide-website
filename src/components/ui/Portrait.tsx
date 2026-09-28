import { useState } from "react";

interface PortraitProps {
  imgSrc?: string;
}

/**
 * Editorial portrait.
 * Drop Victoria's photo at `/public/images/victoria-portrait.jpg` and it is
 * used automatically. Until then, a composed placeholder with the intended
 * proportions and a `[VICTORIA PORTRAIT]` label is shown — swap and re-deploy.
 */
export function Portrait({ imgSrc = "/images/victoria-portrait.jpg" }: PortraitProps) {
  const [failed, setFailed] = useState(false);
  const showImage = imgSrc && !failed;

  return (
    <figure className="portrait">
      {showImage ? (
        <img
          className="portrait__img"
          src={imgSrc}
          alt="Victoria Olamide — product marketing and go-to-market strategist building with Agentic AI"
          loading="eager"
          onError={() => setFailed(true)}
        />
      ) : (
        <div className="portrait__ph" role="img" aria-label="Victoria Olamide portrait">
          <div className="portrait__ph-tone" aria-hidden="true" />
          <div className="portrait__ph-frame" aria-hidden="true" />
          <span className="portrait__ph-label">[ Victoria Portrait ]</span>
          <span className="portrait__ph-role">Product Marketing · GTM · Agentic AI</span>
        </div>
      )}
    </figure>
  );
}